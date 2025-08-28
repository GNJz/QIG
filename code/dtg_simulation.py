import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, UTC

from lif_model import LIFNeuron, dynamic_threshold
from utils import ensure_dir, write_csv_append, save_json, new_run_id

# ===== 고정 파라미터(재현성) =====
DT          = 1e-3       # 1 ms
T_END       = 1.0        # 1 s
TAU         = 20e-3
V_TH_BASE   = 1.0
I_CONST     = 1.10       # 안정 스파이킹 기본값(필요 시 조정)
ALPHAS      = [1.0, 0.7, 0.5]
REFRACT_MS  = 2.0        # 2 ms 불응기 (0이면 비활성)

# ===== 경로 =====
FIG_DIR     = "figures"
SPIKE_CSV   = "data/spikes.csv"
ENERGY_CSV  = "data/energy.csv"
CONFIG_JSON = "data/config.json"


def run_one(alpha: float, run_id: str):
    t = np.arange(0.0, T_END, DT)
    th = dynamic_threshold(t, v_th_base=V_TH_BASE, alpha=alpha)

    neuron = LIFNeuron(
        dt=DT, tau=TAU, v_rest=0.0, v_reset=0.0,
        v_th_base=V_TH_BASE, refractory_ms=REFRACT_MS
    )

    v_trace = np.empty_like(t)
    spikes_mask = np.zeros_like(t, dtype=bool)

    for i, v_th in enumerate(th):
        v, spiked = neuron.step(I=I_CONST, v_th=v_th)
        v_trace[i] = v
        if spiked:
            spikes_mask[i] = True

    total_spikes = int(spikes_mask.sum())
    energy_proxy = float(total_spikes)  # 아주 단순한 근사: 스파이크 수

    # ----- 그림 저장 -----
    fig_path = os.path.join(FIG_DIR, f"membrane_alpha_{alpha}.png")
    ensure_dir(fig_path)  # 파일 경로를 받아 디렉토리를 보장
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, v_trace, label="V(t)")
    ax.plot(t, th, "--", label="V_th(t)")
    if total_spikes > 0:
        ax.scatter(t[spikes_mask], th[spikes_mask], s=10, label="spike")
    ax.set_xlabel("time (s)")
    ax.set_ylabel("V")
    ax.set_title(f"Membrane Potential (alpha={alpha})")
    ax.legend()
    fig.tight_layout()
    fig.savefig(fig_path, dpi=160)
    plt.close(fig)

    # ----- CSV 누적 저장 -----
    ts = datetime.now(UTC).isoformat()
    write_csv_append(
        SPIKE_CSV,
        header=["run_id", "timestamp", "alpha", "spikes"],
        rows=[[run_id, ts, alpha, total_spikes]],
    )
    write_csv_append(
        ENERGY_CSV,
        header=["run_id", "timestamp", "alpha", "energy_proxy"],
        rows=[[run_id, ts, alpha, energy_proxy]],
    )

    print(f"[alpha={alpha}] spikes={total_spikes}, energy_proxy={energy_proxy}, fig={fig_path}")
    return total_spikes, energy_proxy


def main():
    run_id = new_run_id()
    save_json(
        CONFIG_JSON,
        {
            "run_id": run_id,
            "generated_at_utc": datetime.now(UTC).isoformat(),
            "params": {
                "DT": DT, "T_END": T_END, "TAU": TAU,
                "V_TH_BASE": V_TH_BASE, "I_CONST": I_CONST,
                "ALPHAS": ALPHAS, "REFRACT_MS": REFRACT_MS,
            },
        },
    )

    for alpha in ALPHAS:
        run_one(alpha, run_id)


if __name__ == "__main__":
    main()
