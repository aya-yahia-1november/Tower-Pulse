{{ config(materialized='table') }}

with dates as (
    select distinct date_trunc('day', created_dt) as dt
    from {{ ref('stg_full_telecom') }}
    where created_dt is not null
)

select
    to_number(to_varchar(dt,'YYYYMMDD'))::int as date_id,
    dt::date as date,
    date_part(year, dt)  as year,
    date_part(month, dt) as month,
    date_part(day, dt)   as day,
    date_part(dow, dt)   as weekday,
    date_part(week, dt)  as week_number,
    case when date_part(dow, dt) in (6,0) then true else false end as is_weekend
from dates
order by date
