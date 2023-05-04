import mock

from src.domain.services.solicitacao_documento_fiscal_service import SolicitacaoDocumentoFiscalService
from src.infra.aurora.repositories.solicitacao_documento_fiscal_repository import SolicitacaoDocumentoFiscalRepository


def solicitacao_documento_fiscal_service_instancia_criar(
        solicitacao_documento_fiscal_repository_mock: SolicitacaoDocumentoFiscalRepository
) -> SolicitacaoDocumentoFiscalService:
    return SolicitacaoDocumentoFiscalService(
        solicitacao_documento_fiscal_repository=solicitacao_documento_fiscal_repository_mock
    )


@mock.patch('src.infra.aurora.repositories.solicitacao_documento_fiscal_repository')
def test_quando_parametro_correto_deve_adicionar_com_sucesso(solicitacao_documento_fiscal_repository_mock) -> None:
    # arrange
    resultado_esperado = 'teste com moq'
    solicitacao_documento_fiscal_service = solicitacao_documento_fiscal_service_instancia_criar(
        solicitacao_documento_fiscal_repository_mock)
    solicitacao_documento_fiscal_repository_mock.adicionar.return_value = 'teste com moq'

    # act
    resultado = solicitacao_documento_fiscal_service.adicionar()

    # assert
    assert resultado == resultado_esperado
