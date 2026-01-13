{{ config(materialized='table') }}

with raw as (

    select
        ID,
        radio,
        MCC,
        MNC,
        TAC,
        CID,
        LON,
        LAT,
        RANGE,
        SAM,
        created,
        updated,
        Country,
        Network,
        drop_calls,
        total_calls,
        drop_rate,
        avg_load,
        signal_strength,
        speed,
        latency,
        QoE,
        coverage_gap,
        signal_quality,
        tower_status,
        priority,
        maintenance_type,
        created_dt,
        updated_dt,
        maintenance_date,
        labor_cost_egp,
        parts_cost_egp,
        downtime_hours,
        vendor,
        notes
    from {{ source('telecom_raw', 'stg_full_telecom') }}

)

select
    id,
    radio,
    mcc,
    mnc,
    tac,
    cid,
    lon,
    lat,
    range       as range_m,
    sam,
    country,
    network     as network_name,
    drop_calls,
    total_calls,
    case
        when drop_rate is null then null
        when drop_rate > 1 and drop_rate <= 100 then drop_rate/100.0
        else drop_rate
    end         as drop_rate,
    avg_load,
    signal_strength,
    speed,
    latency,
    QoE,
    IFF(coverage_gap::BOOLEAN, TRUE, FALSE) AS coverage_gap,
    signal_quality,
    tower_status,
    priority,
    maintenance_type,
    TO_TIMESTAMP(created_dt)       as created_dt,
    TO_TIMESTAMP(updated_dt)       as updated_dt,
    TO_TIMESTAMP(maintenance_date) as maintenance_date,
    labor_cost_egp,
    parts_cost_egp,
    downtime_hours,
    vendor,
    notes
from raw
