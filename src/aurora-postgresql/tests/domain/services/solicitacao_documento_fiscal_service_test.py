import mock

from src.domain.services.solicitacao_documento_fiscal_service import SolicitacaoDocumentoFiscalService


@mock.patch('src.infra.aurora.repositories.solicitacao_documento_fiscal_repository')
def test_quando_parametro_correto_deve_adicionar_com_sucesso(solicitacao_documento_fiscal_repository_mock) -> None:
    # arrange
    resultado_esperado = 'teste com moq'
    solicitacao_documento_fiscal_repository_mock.adicionar.return_value = 'teste com moq'
    solicitacao_documento_fiscal_service = SolicitacaoDocumentoFiscalService(
        solicitacao_documento_fiscal_repository=solicitacao_documento_fiscal_repository_mock)

    # act
    resultado = solicitacao_documento_fiscal_service.adicionar()

    # assert
    assert resultado == resultado_esperado
