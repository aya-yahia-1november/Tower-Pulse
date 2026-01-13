{{ config(materialized='table') }}

with networks as (
    select distinct
        mcc,
        mnc,
        radio,
        signal_strength,
        network_name,
        drop_calls,
        total_calls,
        drop_rate,
        avg_load,
        speed,
        latency,
        qoe
    from {{ ref('stg_full_telecom') }}
)

select
    row_number() over (order by mcc, mnc, radio) as network_id,
    mcc,
    mnc,
    radio,
    signal_strength,
    network_name as network,
    drop_calls,
    total_calls,
    drop_rate,
    avg_load,
    speed,
    latency,
    qoe
from networks
