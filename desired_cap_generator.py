from selenium.webdriver.common.by import By
#brand_name = "ETRAVEL"
#build_name = "custom build"

desired_cap2 = {
"os" : "Windows",
"os_version" : "11",
"browser" : "Edge",
"browser_version" : "latest",
"resolution" : "1680x1050",
"project" : "sss",
"build" : "buid",
"name" : "name",
"browserstack.local" : "false",
"browserstack.debug" : "true",
"browserstack.networkLogs" : "true",
"browserstack.selenium_version" : "3.5.2"
}



def desired_cap_Branded(brand_name, build_name):
    desired_cap = {
        "os" : "Windows",
        "os_version" : "11",
        "browser" : "Edge",
        "browser_version" : "latest",
        "resolution" : "1680x1050",
        "project": brand_name,
        "build": build_name,
        "name": "Name",
        "browserstack.local": "false",
        "browserstack.networkLogs": "true",
        "browserstack.selenium_version": "3.14.0"
    }
    print (desired_cap)
    return(desired_cap)

#desired_cap_Branded(brand_name, build_name)
#desired_cap_Branded("KTGSk", "Custom build")