import argparse


if __name__=="__main__":
	
	parser = argparse.ArgumentParser(description='TextScan: Scan Text, one file at a time')

	parser.add_argument("filename", help='Enter the filename')
	parser.add_argument("-s", "--summarize", help="Summarize the text", action="store_true")
	parser.add_argument("-n", "--number", help="Number of lines", type = int, required=True)

	args = parser.parse_args()

	if args.summarize:
		
		f = open(args.filename, 'r')
		text = f.read()

		text = text.replace('\n', "")