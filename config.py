import os	

api_key = "98ff232f9d7241e165225e7f42731c5d242c94d0aed9ba54b4276a0039bac746"
#dbusr = "xiadhlaufizfkb"	
#dbpwd = "92881d48fefc1ddb4c84a26d890c076a1f58752d0177af6f6d889afaf4ba6912"	
#dbhost = "ec2-52-203-165-126.compute-1.amazonaws.com"	
#dbengine = "postgresql"	
#db = "d7jnpv43d162ca"
dbusr = "postgres"	
dbpwd = "postgres"	
dbhost = "localhost"	
dbengine = "postgresql"	
db = "postgres"
cxnstring = (os.environ["DATABASE_URL"] if os.getenv("DATABASE_URL")	
    else f"{dbengine}://{dbusr}:{dbpwd}@{dbhost}/{db}")