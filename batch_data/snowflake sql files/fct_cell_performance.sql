{{ config(materialized='table') }}

with src as (
    select * from {{ ref('stg_fact_source') }}
),

joined as (
    select
        s.original_id,
        t.tower_id,
        n.network_id,
        s.date_id,
        m.maintenance_id,
        s.created_ts
    from src s
    left join {{ ref('dim_tower') }} t
        on t.cid = s.cid and t.tac = s.tac
    left join {{ ref('dim_network') }} n
        on n.mcc = s.mcc and n.mnc = s.mnc and n.radio = s.radio
    left join {{ ref('dim_maintenance') }} m
        on m.maintenance_type = s.maintenance_type and m.priority = s.priority
)

select
    row_number() over(order by created_ts, original_id) as fact_id,
    *
from joined
