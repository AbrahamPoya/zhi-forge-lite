from pydantic import BaseModel, Field

class ZhiLearningEnergyModel(BaseModel):
    mu: float = Field(..., description="μ(t): 運算增益函數")
    nu: float = Field(..., description="ν(t): 熵干擾權重")
    phi: float = Field(..., description="φ(t): 語境調和調整器")

    def compute_dE_dt(
        self,
        df_turing_dt: float,
        dH_semantic_dt: float,
        d_epsilon_drift_dt: float
    ) -> float:
        return (
            self.mu * df_turing_dt
            - self.nu * dH_semantic_dt
            + self.phi * d_epsilon_drift_dt
        )