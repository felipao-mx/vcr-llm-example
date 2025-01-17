import pytest

from main import invoke_anthropic_model, invoke_openai_agent, invoke_openai_model


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization", "x-api-key"],
        "filter_query_parameters": ["api-key", "access_token"],
    }


@pytest.mark.vcr
def test_invoke_anthropic_model():
    result = invoke_anthropic_model()
    assert result.content == "Ciao!"


@pytest.mark.vcr
def test_invoke_openai_model():
    result = invoke_openai_model()
    assert result.content == "Ciao!"


@pytest.mark.vcr
def test_invoke_openai_agent():
    result = invoke_openai_agent()
    assert result.return_values == {'output': 'The capital of France is Paris.'}

