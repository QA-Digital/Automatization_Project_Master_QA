import unittest
import HtmlTestRunner
#import HTMLTestRunner as HtmlTestRunner        ##setting for office pc since the packaga installed with diff name (i guess?)



def runner_tests_generalized(suite_general, web_brand, version, URL):
    runner = unittest.TextTestRunner()
    outfile = open("results.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title=web_brand + " ||| " + URL,
                                           report_name="WEB Suite Report - version --- " + version + " ---",
                                           open_in_browser=True, description=web_brand+ " WEB Suite Report - version --- " + version + " ---")
    runner.run(suite_general())


