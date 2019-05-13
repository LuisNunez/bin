# Powershell Script to parse a CSV file.

%test_csv = import-CSV .\test.csv

foreach ($TanObject in $test_csv)
  (
    write-host 'TanObject.Result: '$TanObject.Result
    write-host ' TanObject.IP Address: '$TanObject.'IP Address'
    $ip_split = %TanObject.'IP Address'.Split(',')
    foreash ($ip_addr in $ip_split)
    	{
    		$ip_version_check = $ip_addr.Contains("::")
    		if ($ip_verion_check -eq "True")
    			{
    				write-host "IPV6" $ip_addr
    			}
    		Else 
    			{
    				write-host "IPV4" $ip_addr
    			}
    	}
