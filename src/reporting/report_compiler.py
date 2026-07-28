"""Report compiler module for compiling match artifacts."""

from src.automation.reporting import GmailReporter


class ReportCompiler:
    """Compiler wrapper for match report artifacts."""

    def __init__(self):
        self.reporter = GmailReporter()

    def compile_match_reports(self, summary_data):
        return self.reporter.compile_match_reports(summary_data)
