from zhi_learning_sdk import ZhiLearningEnergyModel

def test_compute_dE_dt():
    model = ZhiLearningEnergyModel(mu=1.0, nu=1.0, phi=1.0)
    result = model.compute_dE_dt(0.5, 0.2, 0.3)
    assert abs(result - 0.6) < 1e-6