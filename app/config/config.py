import os
from typing import Any, Optional
from dotenv import load_dotenv


class EnvManager:
    """
    Classe per gestire l'accesso alle variabili d'ambiente attraverso l'intera applicazione.
    Utilizza il pattern Singleton per assicurare una singola istanza.
    """
    _instance = None
    _initialized = False

    def __new__(cls, env_path: Optional[str] = None):
        if cls._instance is None:
            cls._instance = super(EnvManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, env_path: Optional[str] = None):
        if not self._initialized:
            # Carica le variabili d'ambiente solo la prima volta
            if env_path:
                load_dotenv(env_path)
            else:
                load_dotenv()
            self._initialized = True
            self._cached_values = {}

    def get(self, key: str, default: Any = None) -> Any:
        """
        Ottiene il valore di una variabile d'ambiente.

        Args:
            key: Il nome della variabile d'ambiente.
            default: Il valore predefinito se la variabile non esiste.

        Returns:
            Il valore della variabile d'ambiente o il valore predefinito.
        """
        # Usa la cache se disponibile
        if key in self._cached_values:
            return self._cached_values[key]

        value = os.getenv(key, default)
        self._cached_values[key] = value
        return value

    def get_int(self, key: str, default: Optional[int] = None) -> Optional[int]:
        """Ottiene una variabile d'ambiente come intero."""
        value = self.get(key, default)
        if value is None:
            return None

        try:
            return int(value)
        except ValueError:
            return default

    def get_float(self, key: str, default: Optional[float] = None) -> Optional[float]:
        """Ottiene una variabile d'ambiente come float."""
        value = self.get(key, default)
        if value is None:
            return None

        try:
            return float(value)
        except ValueError:
            return default

    def get_bool(self, key: str, default: Optional[bool] = None) -> Optional[bool]:
        """Ottiene una variabile d'ambiente come booleano."""
        value = self.get(key, default)
        if value is None:
            return None

        if isinstance(value, bool):
            return value

        return value.lower() in ('true', 'yes', '1', 'y', 't')

    def get_list(self, key: str, separator: str = ',', default: Optional[list] = None) -> Optional[list]:
        """Ottiene una variabile d'ambiente come lista di stringhe."""
        value = self.get(key)
        if value is None:
            return default if default is not None else []

        return [item.strip() for item in value.split(separator)]

    def refresh(self, env_path: Optional[str] = None) -> None:
        """
        Ricarica le variabili d'ambiente dal file .env.
        Utile se il file .env è stato modificato durante l'esecuzione.
        """
        if env_path:
            load_dotenv(env_path, override=True)
        else:
            load_dotenv(override=True)

        # Pulisci la cache
        self._cached_values = {}


### UTILIZZO ###

# # Nel file principale (es. app.py)
# from env_manager import EnvManager
#
# # Inizializza il gestore all'avvio dell'applicazione
# env = EnvManager()  # O EnvManager("/path/personalizzato/.env")
#
# # In qualsiasi altra classe o file
# from env_manager import EnvManager
#
# class Database:
#     def __init__(self):
#         env = EnvManager()  # Otterrai la stessa istanza inizializzata in precedenza
#         self.connection_string = env.get("DATABASE_URL")
#         self.pool_size = env.get_int("DB_POOL_SIZE", 10)  # default a 10
#         self.debug = env.get_bool("DEBUG", False)
#
# class ApiClient:
#     def __init__(self):
#         env = EnvManager()
#         self.api_key = env.get("API_KEY")
#         self.timeout = env.get_float("API_TIMEOUT", 30.0)
#         self.allowed_hosts = env.get_list("ALLOWED_HOSTS")