from models.base import BaseCalDav
import caldav

# ---------------------------------------------------------------------------- #
#                                 iCloudCalDav                                 #
# ---------------------------------------------------------------------------- #
class InfomaniakCalDav(BaseCalDav):
	def connect(self):
		self.client = caldav.DAVClient(
			url="https://sync.infomaniak.com",
			username=self.username,
			password=self.password
		)
		super().connect()
