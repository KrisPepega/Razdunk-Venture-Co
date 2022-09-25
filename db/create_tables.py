from database import engine
import models

models.BASE.metadata.create_all(engine)