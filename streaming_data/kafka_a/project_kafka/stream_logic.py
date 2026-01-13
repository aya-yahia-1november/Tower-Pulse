import numpy as np
import pandas as pd
import time


def stream_tower_updates(df, n=5):
    df = df.copy()

    sample = df.sample(n).copy()
    now_ts = int(time.time())
    now_dt = pd.Timestamp.now()

    for i in sample.index:

        sample.loc[i, "updated"] = now_ts
        sample.loc[i, "updated_dt"] = now_dt

        sample.loc[i, "drop_calls"] = max(
            0, sample.loc[i, "drop_calls"] + np.random.randint(-2, 6)
        )

        sample.loc[i, "total_calls"] = max(
            sample.loc[i, "drop_calls"] + 1,
            sample.loc[i, "total_calls"] + np.random.randint(-10, 30)
        )

        sample.loc[i, "drop_rate"] = round(
            sample.loc[i, "drop_calls"] / sample.loc[i, "total_calls"], 4
        )

        sample.loc[i, "avg_load"] = round(
            min(1, max(0, sample.loc[i, "avg_load"] + np.random.uniform(-0.05, 0.08))), 3
        )

        sample.loc[i, "signal_strength"] = np.random.randint(-110, -40)
        sample.loc[i, "speed"] = round(np.random.uniform(2, 150), 2)
        sample.loc[i, "latency"] = round(np.random.uniform(10, 150), 2)

        sample.loc[i, "QoE"] = round(
            np.random.uniform(1, 5) - sample.loc[i, "drop_rate"] * 1.5, 2
        )

        sample.loc[i, "coverage_gap"] = sample.loc[i, "signal_strength"] < -100

        if sample.loc[i, "QoE"] > 4:
            sample.loc[i, "signal_quality"] = "Excellent"
        elif sample.loc[i, "QoE"] > 3:
            sample.loc[i, "signal_quality"] = "Good"
        elif sample.loc[i, "QoE"] > 2:
            sample.loc[i, "signal_quality"] = "Fair"
        else:
            sample.loc[i, "signal_quality"] = "Poor"

        sample.loc[i, "tower_status"] = np.random.choice(
            ["active", "warning", "down"], p=[0.85, 0.10, 0.05]
        )

        if sample.loc[i, "tower_status"] == "down":
            sample.loc[i, "priority"] = "critical"
        elif sample.loc[i, "drop_rate"] > 0.1 or sample.loc[i, "avg_load"] > 0.85:
            sample.loc[i, "priority"] = "high"
        elif sample.loc[i, "drop_rate"] > 0.05:
            sample.loc[i, "priority"] = "medium"
        else:
            sample.loc[i, "priority"] = "low"

        sample.loc[i, "maintenance_date"] = now_dt - pd.Timedelta(
            days=np.random.randint(1, 120)
        )

        sample.loc[i, "labor_cost_egp"] = int(
            sample.loc[i, "labor_cost_egp"] * np.random.uniform(0.95, 1.1)
        )

        sample.loc[i, "parts_cost_egp"] = int(
            sample.loc[i, "parts_cost_egp"] * np.random.uniform(0.9, 1.2)
        )

        sample.loc[i, "downtime_hours"] = round(
            sample.loc[i, "downtime_hours"] * np.random.uniform(0.8, 1.2), 1
        )

        if np.random.random() < 0.08:
            sample.loc[i, "notes"] = np.random.choice([
                "Temporary power fluctuation",
                "Minor transmission delay observed",
                "Environmental interference",
                "Cooling system alert",
                ""
            ])

    return sample



