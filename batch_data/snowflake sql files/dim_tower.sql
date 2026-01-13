{{ config(materialized='table') }}

with towers as (
    select distinct
        cid,
        tac,
        country,
        lon,
        lat,
        range_m,
        sam,
        tower_status,
        signal_quality,
        coverage_gap
    from {{ ref('stg_full_telecom') }}
)

select
    row_number() over (order by cid, tac) as tower_id,
    cid,
    tac,
    country,
    lon,
    lat,
    range_m as range,
    sam,
    tower_status,
    signal_quality,
    coverage_gap
from towers
