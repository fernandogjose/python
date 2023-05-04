from src.infra.aurora.repositories.solicitacao_documento_fiscal_repository import SolicitacaoDocumentoFiscalRepository


class SolicitacaoDocumentoFiscalService:
    def __init__(self, solicitacao_documento_fiscal_repository: SolicitacaoDocumentoFiscalRepository = None):
        self.solicitacao_documento_fiscal_repository = solicitacao_documento_fiscal_repository or \
                                                       SolicitacaoDocumentoFiscalRepository()

    def adicionar(self) -> str:
        return self.solicitacao_documento_fiscal_repository.adicionar()
