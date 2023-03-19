import sys


class Parser:
	def __init__(self):
		self.csv_file_name = ""
		self.markdown_file_name = ""

	def parse_args(self, args: list[str]) -> tuple[str, str]:
		try:
			self.check_args(args)
			return (args[0], args[1])
		except IOError as io_error:
			print(io_error)
			sys.exit()

	def check_args(self, args: list[str]) -> None:
		if not args or len(args) != 2:
			raise IOError("argument error")
		elif not args[0].endswith(".csv"):
			raise IOError("csv format error")
		elif not args[1].endswith(".md"):
			raise IOError("markdown format error")
