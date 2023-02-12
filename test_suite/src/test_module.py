from gailbot.plugins.plugin import Plugin
from typing import Any, Dict
from gailbot.plugins.plugin import Methods
from gailbot.core.utils.logger import makelogger

logger = makelogger("individual_test_plugins")

class test(Plugin):
    def __init__(self) -> None:
        super().__init__()
        self.name = "default test"
        
    def apply(self, dependency_outputs: Dict[str, Any], methods: Methods, *args, **kwargs) -> Any:
        super().apply(dependency_outputs, methods, *args, **kwargs)
        logger.info(f"test plugin {self.name}")
