from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./test.db"
    echo: bool = True



settings = Settings()

# # Строка подключения к базе данных SQLite
# DATABASE_URL = "sqlite:///./test.db"
#
# # Создаем движок SQLite
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # Базовый класс для всех моделей
# Base = declarative_base()
#
# # Создаем функцию для получения сессии базы данных
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()