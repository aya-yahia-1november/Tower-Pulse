{{ config(materialized='table') }}

select
    id as original_id,
    cid,
    tac,
    mcc,
    mnc,
    radio,
    maintenance_type,
    priority,
    to_timestamp(created_dt) as created_ts,
    to_number(to_varchar(date_trunc('day', to_timestamp(created_dt)), 'YYYYMMDD'))::int as date_id
from {{ ref('stg_full_telecom') }}
where created_dt is not null
