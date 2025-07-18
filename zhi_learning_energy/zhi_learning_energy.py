import typer
from zhi_learning_sdk import ZhiLearningEnergyModel

app = typer.Typer()

@app.command()
def simulate(
    df_turing: float = typer.Option(0.0, help="df(Turing)/dt: 核心運算變化率"),
    dH_semantic: float = typer.Option(0.0, help="dH_semantic/dt: 語義熵變化率"),
    d_epsilon_drift: float = typer.Option(0.0, help="dε_context_drift/dt: 語境漂移變化率"),
    mu: float = typer.Option(1.0, help="μ(t): 運算增益函數"),
    nu: float = typer.Option(1.0, help="ν(t): 熵干擾權重"),
    phi: float = typer.Option(1.0, help="φ(t): 語境調和調整器")
):
    model = ZhiLearningEnergyModel(mu=mu, nu=nu, phi=phi)
    dE_dt = model.compute_dE_dt(df_turing, dH_semantic, d_epsilon_drift)
    typer.echo(f"🔹 語義能態變化率 dE_AGI/dt = {dE_dt:.4f}")

if __name__ == "__main__":
    app()