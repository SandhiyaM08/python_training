'''invited={"Alice","Bob","Charlie"}
arrived={"Alice","Charlie","Diana"}
unexpected=invited-arrived
if unexpected:
   print("Unexpected guests arrived:",unexpected)'''

invited={"Alice","Bob","Charlie"}
arrived={"Alice","Charlie","Diana"}
if invited not in arrived:
   print("Unexpected guests arrived",)