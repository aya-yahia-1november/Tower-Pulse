{{ config(materialized='table') }}

with maint as (
    select distinct
        maintenance_type,
        priority,
        labor_cost_egp,
        parts_cost_egp,
        downtime_hours,
        vendor,
        notes
    from {{ ref('stg_full_telecom') }}
)

select
    row_number() over (order by maintenance_type, priority) as maintenance_id,
    maintenance_type,
    priority,
    labor_cost_egp,
    parts_cost_egp,
    downtime_hours,
    vendor,
    notes
from maint
