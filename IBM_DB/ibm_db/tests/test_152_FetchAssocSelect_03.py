# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

from __future__ import print_function
import sys
import unittest
import ibm_db
import config
from testfunctions import IbmDbTestFunctions

class IbmDbTestCase(unittest.TestCase):

  def test_152_FetchAssocSelect_03(self):
    obj = IbmDbTestFunctions()
    obj.assert_expect(self.run_test_152)

  def run_test_152(self):
    conn = ibm_db.connect(config.database, config.user, config.password)

    server = ibm_db.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'IDS'):
      op = {ibm_db.ATTR_CASE: ibm_db.CASE_UPPER}
      ibm_db.set_option(conn, op, 1)
    
    result = ibm_db.exec_immediate(conn, "select * from project")
    
    row = ibm_db.fetch_assoc(result)
    while ( row ):
      #printf("%6s ",row['PROJNO'])
      #printf("%-24s ",row['PROJNAME'])
      #printf("%3s ",row['DEPTNO'])
      #printf("%6s",row['RESPEMP'])
      #printf("%7s ",row['PRSTAFF'])
      #printf("%10s ",row['PRSTDATE'])
      #printf("%10s ",row['PRENDATE'])
      #printf("%6s",row['MAJPROJ'])
      #puts ""
      if (row['MAJPROJ'] == None):
        row['MAJPROJ'] = ''
      print("%6s %-24s %3s %6s%7s %10s %10s %6s" % (row['PROJNO'], row['PROJNAME'], row['DEPTNO'], row['RESPEMP'], row['PRSTAFF'], row['PRSTDATE'], row['PRENDATE'], row['MAJPROJ']))
      row = ibm_db.fetch_assoc(result) 

#__END__
#__LUW_EXPECTED__
#
#AD3100 ADMIN SERVICES           D01 000010   6.50 1982-01-01 1983-02-01       
#AD3110 GENERAL ADMIN SYSTEMS    D21 000070   6.00 1982-01-01 1983-02-01 AD3100
#AD3111 PAYROLL PROGRAMMING      D21 000230   2.00 1982-01-01 1983-02-01 AD3110
#AD3112 PERSONNEL PROGRAMMING    D21 000250   1.00 1982-01-01 1983-02-01 AD3110
#AD3113 ACCOUNT PROGRAMMING      D21 000270   2.00 1982-01-01 1983-02-01 AD3110
#IF1000 QUERY SERVICES           C01 000030   2.00 1982-01-01 1983-02-01       
#IF2000 USER EDUCATION           C01 000030   1.00 1982-01-01 1983-02-01       
#MA2100 WELD LINE AUTOMATION     D01 000010  12.00 1982-01-01 1983-02-01       
#MA2110 W L PROGRAMMING          D11 000060   9.00 1982-01-01 1983-02-01 MA2100
#MA2111 W L PROGRAM DESIGN       D11 000220   2.00 1982-01-01 1982-12-01 MA2110
#MA2112 W L ROBOT DESIGN         D11 000150   3.00 1982-01-01 1982-12-01 MA2110
#MA2113 W L PROD CONT PROGS      D11 000160   3.00 1982-02-15 1982-12-01 MA2110
#OP1000 OPERATION SUPPORT        E01 000050   6.00 1982-01-01 1983-02-01       
#OP1010 OPERATION                E11 000090   5.00 1982-01-01 1983-02-01 OP1000
#OP2000 GEN SYSTEMS SERVICES     E01 000050   5.00 1982-01-01 1983-02-01       
#OP2010 SYSTEMS SUPPORT          E21 000100   4.00 1982-01-01 1983-02-01 OP2000
#OP2011 SCP SYSTEMS SUPPORT      E21 000320   1.00 1982-01-01 1983-02-01 OP2010
#OP2012 APPLICATIONS SUPPORT     E21 000330   1.00 1982-01-01 1983-02-01 OP2010
#OP2013 DB/DC SUPPORT            E21 000340   1.00 1982-01-01 1983-02-01 OP2010
#PL2100 WELD LINE PLANNING       B01 000020   1.00 1982-01-01 1982-09-15 MA2100
#__ZOS_EXPECTED__
#
#AD3100 ADMIN SERVICES           D01 000010   6.50 1982-01-01 1983-02-01       
#AD3110 GENERAL ADMIN SYSTEMS    D21 000070   6.00 1982-01-01 1983-02-01 AD3100
#AD3111 PAYROLL PROGRAMMING      D21 000230   2.00 1982-01-01 1983-02-01 AD3110
#AD3112 PERSONNEL PROGRAMMING    D21 000250   1.00 1982-01-01 1983-02-01 AD3110
#AD3113 ACCOUNT PROGRAMMING      D21 000270   2.00 1982-01-01 1983-02-01 AD3110
#IF1000 QUERY SERVICES           C01 000030   2.00 1982-01-01 1983-02-01       
#IF2000 USER EDUCATION           C01 000030   1.00 1982-01-01 1983-02-01       
#MA2100 WELD LINE AUTOMATION     D01 000010  12.00 1982-01-01 1983-02-01       
#MA2110 W L PROGRAMMING          D11 000060   9.00 1982-01-01 1983-02-01 MA2100
#MA2111 W L PROGRAM DESIGN       D11 000220   2.00 1982-01-01 1982-12-01 MA2110
#MA2112 W L ROBOT DESIGN         D11 000150   3.00 1982-01-01 1982-12-01 MA2110
#MA2113 W L PROD CONT PROGS      D11 000160   3.00 1982-02-15 1982-12-01 MA2110
#OP1000 OPERATION SUPPORT        E01 000050   6.00 1982-01-01 1983-02-01       
#OP1010 OPERATION                E11 000090   5.00 1982-01-01 1983-02-01 OP1000
#OP2000 GEN SYSTEMS SERVICES     E01 000050   5.00 1982-01-01 1983-02-01       
#OP2010 SYSTEMS SUPPORT          E21 000100   4.00 1982-01-01 1983-02-01 OP2000
#OP2011 SCP SYSTEMS SUPPORT      E21 000320   1.00 1982-01-01 1983-02-01 OP2010
#OP2012 APPLICATIONS SUPPORT     E21 000330   1.00 1982-01-01 1983-02-01 OP2010
#OP2013 DB/DC SUPPORT            E21 000340   1.00 1982-01-01 1983-02-01 OP2010
#PL2100 WELD LINE PLANNING       B01 000020   1.00 1982-01-01 1982-09-15 MA2100
#__SYSTEMI_EXPECTED__
#
#AD3100 ADMIN SERVICES           D01 000010   6.50 1982-01-01 1983-02-01       
#AD3110 GENERAL ADMIN SYSTEMS    D21 000070   6.00 1982-01-01 1983-02-01 AD3100
#AD3111 PAYROLL PROGRAMMING      D21 000230   2.00 1982-01-01 1983-02-01 AD3110
#AD3112 PERSONNEL PROGRAMMING    D21 000250   1.00 1982-01-01 1983-02-01 AD3110
#AD3113 ACCOUNT PROGRAMMING      D21 000270   2.00 1982-01-01 1983-02-01 AD3110
#IF1000 QUERY SERVICES           C01 000030   2.00 1982-01-01 1983-02-01       
#IF2000 USER EDUCATION           C01 000030   1.00 1982-01-01 1983-02-01       
#MA2100 WELD LINE AUTOMATION     D01 000010  12.00 1982-01-01 1983-02-01       
#MA2110 W L PROGRAMMING          D11 000060   9.00 1982-01-01 1983-02-01 MA2100
#MA2111 W L PROGRAM DESIGN       D11 000220   2.00 1982-01-01 1982-12-01 MA2110
#MA2112 W L ROBOT DESIGN         D11 000150   3.00 1982-01-01 1982-12-01 MA2110
#MA2113 W L PROD CONT PROGS      D11 000160   3.00 1982-02-15 1982-12-01 MA2110
#OP1000 OPERATION SUPPORT        E01 000050   6.00 1982-01-01 1983-02-01       
#OP1010 OPERATION                E11 000090   5.00 1982-01-01 1983-02-01 OP1000
#OP2000 GEN SYSTEMS SERVICES     E01 000050   5.00 1982-01-01 1983-02-01       
#OP2010 SYSTEMS SUPPORT          E21 000100   4.00 1982-01-01 1983-02-01 OP2000
#OP2011 SCP SYSTEMS SUPPORT      E21 000320   1.00 1982-01-01 1983-02-01 OP2010
#OP2012 APPLICATIONS SUPPORT     E21 000330   1.00 1982-01-01 1983-02-01 OP2010
#OP2013 DB/DC SUPPORT            E21 000340   1.00 1982-01-01 1983-02-01 OP2010
#PL2100 WELD LINE PLANNING       B01 000020   1.00 1982-01-01 1982-09-15 MA2100
#__IDS_EXPECTED__
#
#AD3100 ADMIN SERVICES           D01 000010   6.50 1982-01-01 1983-02-01       
#AD3110 GENERAL ADMIN SYSTEMS    D21 000070   6.00 1982-01-01 1983-02-01 AD3100
#AD3111 PAYROLL PROGRAMMING      D21 000230   2.00 1982-01-01 1983-02-01 AD3110
#AD3112 PERSONNEL PROGRAMMING    D21 000250   1.00 1982-01-01 1983-02-01 AD3110
#AD3113 ACCOUNT PROGRAMMING      D21 000270   2.00 1982-01-01 1983-02-01 AD3110
#IF1000 QUERY SERVICES           C01 000030   2.00 1982-01-01 1983-02-01       
#IF2000 USER EDUCATION           C01 000030   1.00 1982-01-01 1983-02-01       
#MA2100 WELD LINE AUTOMATION     D01 000010  12.00 1982-01-01 1983-02-01       
#MA2110 W L PROGRAMMING          D11 000060   9.00 1982-01-01 1983-02-01 MA2100
#MA2111 W L PROGRAM DESIGN       D11 000220   2.00 1982-01-01 1982-12-01 MA2110
#MA2112 W L ROBOT DESIGN         D11 000150   3.00 1982-01-01 1982-12-01 MA2110
#MA2113 W L PROD CONT PROGS      D11 000160   3.00 1982-02-15 1982-12-01 MA2110
#OP1000 OPERATION SUPPORT        E01 000050   6.00 1982-01-01 1983-02-01       
#OP1010 OPERATION                E11 000090   5.00 1982-01-01 1983-02-01 OP1000
#OP2000 GEN SYSTEMS SERVICES     E01 000050   5.00 1982-01-01 1983-02-01       
#OP2010 SYSTEMS SUPPORT          E21 000100   4.00 1982-01-01 1983-02-01 OP2000
#OP2011 SCP SYSTEMS SUPPORT      E21 000320   1.00 1982-01-01 1983-02-01 OP2010
#OP2012 APPLICATIONS SUPPORT     E21 000330   1.00 1982-01-01 1983-02-01 OP2010
#OP2013 DB/DC SUPPORT            E21 000340   1.00 1982-01-01 1983-02-01 OP2010
#PL2100 WELD LINE PLANNING       B01 000020   1.00 1982-01-01 1982-09-15 MA2100
