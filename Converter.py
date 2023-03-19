import csv, io

class Converter:
	def __init__(self, ignored_fields: list[str]):
		self.ignored_fields = ignored_fields
		self.table_head: list[str] = []
		self.table_data: list[list[str]] = []

	def read_csv(self, file_name: str):
		with open(file_name, newline='') as csv_file:
			csv_reader = csv.reader(csv_file)
			header = next(csv_reader, None)
			if header: self.table_head.extend(header)
			for row in csv_reader: self.table_data.append(row)

	def convert_csv_to_md(self, md_file_name: str):
		for i, table_row in enumerate(self.table_data):
			file_name = md_file_name.strip(".md") if md_file_name else "csv_to_md.md"
			with io.open(f"{i}_{file_name}.md", 'w', encoding="utf-8") as md_file:
				for heading, paragraph in zip(self.table_head, table_row):
					if heading in self.ignored_fields: continue
					md_file.write('# ' + heading + '  \n')
					md_file.write(paragraph + '  \n')
