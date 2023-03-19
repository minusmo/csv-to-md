import sys
import Parser
import Converter

def main():
	csv_file_name = input("csv file to be converted: ").strip()
	markdown_file_name = input("markdown file to be created: ").strip()
	ignored_fields = input("ignored fields: ").strip().split()
	try:
		parser = Parser.Parser()
		parser.check_args([csv_file_name, markdown_file_name])
		converter = Converter.Converter(ignored_fields)
		converter.read_csv(csv_file_name)
		converter.convert_csv_to_md(markdown_file_name)
	except IOError:
		print("file IO error")
		sys.exit()


if __name__ == '__main__':
	main()
