import urllib.request,urllib.parse, socket
import re,os,sys
def emailgrabber():
	os.system("clear")
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

		banner="""
{

########
##      ## *************************************
#       ##    __Tutorial/Channel__[youtube.com/anonymousbghh]
########
########
#       ##    __Repository__[https://github.com/josifkhan/]
##      ##    __Author_Name__[MD Josif Khan]
########_______________}

_________                    ________________________________
		                                        BANgLADESH
		                                           V1.0	}




		"""
		print(banner)
		url=input("\nTarget Website: ")
		if url=="":
			print("Target Undetected.")
			input("		Enter to exit.")
			sys.exit("done.")

		elif not url.startswith("http"):
			print(f"Cannot continue with target '{url}' Try target including http:// or https://")
			input("\n\nEnter to exit...")
			sys.exit("done.")
		else:
			connect=urllib.request.Request(url, headers=headers)
			webpages=urllib.request.urlopen(connect).read().decode('utf-8')
			targetwords=re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+[-a-zA-Z0-9._]+")
			grabber=re.findall(targetwords, webpages)
			if len(grabber)==0:
				print(f"No email found on this site {url}.")
				input("\n\nEnter to exit...")
				sys.exit("done.")
			else:
				print(grabber)
				input("\n\nEnter to exit...")
				sys.exit("done.")
	except socket.gaierror:
		print("\nNo network connection found. Enable internet")
		input("\n\nEnter to exit...")
		sys.exit("done.")

	except urllib.error.URLError:
		print(f"""\nWe can’t connect to the server at {url}.
If that address is correct, here are two other things you can try:

    Try again later.
    Check your network connection.""")
		input("\n\nEnter to exit...")
		sys.exit("done.")

	except ValueError:
		print(f"Cannot continue with target '{url}' Try target including http:// or https://")
		input("\n\nEnter to exit...")
		sys.exit("done.")

	except KeyboardInterrupt:
		input("\n\nEnter to exit...")
		sys.exit("done.")




emailgrabber()
