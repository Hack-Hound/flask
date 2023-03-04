import sqlite3
import os
import time


class DB_Manager:
    def __init__(self):
        self.conn = sqlite3.connect(
            (str(os.path.dirname(os.path.abspath(__file__)))+'/config.db'))

    # record table creation
    def TableCreation(self):
        self.conn.execute('''CREATE TABLE ITEM
                (ID         INTEGER     PRIMARY KEY     AUTOINCREMENT,
                Name        TEXT        UNIQUE          NOT NULL,
                Price       INTEGER     UNIQUE          NOT NULL,
                Description TEXT                        NOT NULL);''')
        print("ITEM Record table created successfully")

        self.conn.execute('''CREATE TABLE ORDER
                (Order_ID       INTEGER     PRIMARY KEY     AUTOINCREMENT,
                Item_ID         INTEGER                     NOT NULL,
                User_ID         INTEGER                     NOT NULL,
                Table_Number    INTEGER     UNIQUE          NOT NULL,
                Order_Status    TEXT                        NOT NULL,
                foreign key(Item_ID) references ITEM(ID));''')
        print("ORDER Record table created successfully")

       

    # Query all

    def QuarryCred(self):
        SUB = self.SqlQuarryExec("""select ID,Name,Salt,Pass
                                from CRED;""")
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB]])

    def QuarryCredPass(self):
        SUB = self.SqlQuarryExec("""select Pass
                                from CRED;""")
        return ([s[0] for s in SUB])

    def QuarryCredSalt(self):
        SUB = self.SqlQuarryExec("""select Salt
                                from CRED;""")
        return ([s[0] for s in SUB])

    def QuarryAllPlugin(self):
        SUB = self.SqlQuarryExec("""select ID,Name,Description,Version,MainFile,Type
                                from PLUGIN
                                order by ID asc;""")
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB]])

    def QuarryPluginByID(self, ID):
        SUB = self.SqlQuarryExec("""select ID,Name,Description,Version,MainFile,Type
                                from PLUGIN
                                where ID={0};""".format(ID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB]])

    def QuarryPluginNameByID(self, ID):
        SUB = self.SqlQuarryExec("""select Name
                                from PLUGIN
                                where ID={0};""".format(ID))
        return ([s[0] for s in SUB])

    def QuarryPluginByIDin(self, IDs):
        s = ""
        for i in range(len(IDs)-1):
            s = s+str(IDs[i])+","
        try:
            t = str(IDs[len(IDs)-1])
        except:
            t = ""
        s = s+t
        print(s)

        SUB = self.SqlQuarryExec("""select ID,Name,Description,Version,MainFile,Type
                                from PLUGIN
                                where ID in ({0});""".format(s))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB]])

    def QuarryPluginIdByIDin(self, IDs):
        s = ""
        for i in range(len(IDs)-1):
            s = s+str(IDs[i])+","
        try:
            t = str(IDs[len(IDs)-1])
        except:
            t = ""
        s = s+t
        print(s)

        SUB = self.SqlQuarryExec("""select ID
                                from PLUGIN
                                where ID in ({0});""".format(s))
        return ([s[0] for s in SUB])

    def QuarryPluginByName(self, Name):
        SUB = self.SqlQuarryExec("""select ID,Name,Description,Version,MainFile,Type
                                from PLUGIN
                                where Name="{0}";""".format(Name))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB]])

    def QuarryPluginIdByName(self, Name):
        SUB = self.SqlQuarryExec("""select ID
                                from PLUGIN
                                where Name="{0}";""".format(Name))
        return ([s[0] for s in SUB])

    def QuarryAllROUTS(self):
        SUB = self.SqlQuarryExec("""select ID,ID_Plugin,URI,Type
                                from ROUTS;""")
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB]])

    def QuarryROUTSByID(self, ID):
        SUB = self.SqlQuarryExec("""select ID,ID_Plugin,URI,Type
                                from ROUTS
                                where ID_Plugin={0};""".format(ID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB]])

    def QuarrySH_FILESByID(self, ID):
        SUB = self.SqlQuarryExec("""select ID,URI_Name,URI_File,UAID
                                from SH_FILES
                                where ID={0};""".format(ID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB]])
    
    def QuarrySH_FILESByUAIDandName(self, UAID, Name):
        try:
            SUB = self.SqlQuarryExec("""select ID,URI_Name,URI_File,UAID
                                    from SH_FILES
                                    where UAID={0} and URI_Name="{1}";""".format(UAID, Name))
            return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB]])
        except:
            return [[],[],[],[]]

    def QuarryTOKENByHASH(self, hash):
        SUB = self.SqlQuarryExec("""select Hash,Name,CreatTime,EndTime,Description,AccessCode,PluginID,UAID
                                from TOKEN
                                where Hash=\"{0}\";""".format(hash))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB], [s[6] for s in SUB], [s[7] for s in SUB]])

    def QuarryHOOKBySID(self, SID):
        SUB = self.SqlQuarryExec("""select SID,Hook,DID,Status,UAID
                                from HOOK
                                where SID={0};""".format(SID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB]])

    def QuarryHOOKByDID(self, DID):
        SUB = self.SqlQuarryExec("""select SID,Hook,DID,Status,UAID
                                from HOOK
                                where DID={0};""".format(DID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB]])

    def QuarryLOGByPluginID(self, PluginID):
        SUB = self.SqlQuarryExec("""select PluginID,Log,TimeStamp,priority,UAID
                                from LOG
                                where PluginID={0};""".format(PluginID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB]])

    def QuarryLOGByPriority(self, priority):
        SUB = self.SqlQuarryExec("""select PluginID,Log,TimeStamp,priority,UAID
                                from LOG
                                where priority={0};""".format(priority))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB]])

    def QuarryLOGByTimeStamps(self, TimeStampInit, TimeStampEnd):
        SUB = self.SqlQuarryExec("""select PluginID,Log,TimeStamp,priority,UAID
                                from LOG
                                where TimeStamp BETWEEN {0} AND {1};""".format(TimeStampInit, TimeStampEnd))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB]])

    def QuarryACCESSByPluginID(self, PluginID):
        SUB = self.SqlQuarryExec("""select PID,UID
                                from ACCESS
                                where PID={0};""".format(PluginID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB]])

    def QuarryACCESSByUserID(self, UserID):
        SUB = self.SqlQuarryExec("""select PID,UID
                                from ACCESS
                                where UID={0};""".format(UserID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB]])

    # adding to Record table

    def AddCred(self, Name, Salt, Pass):
        try:
            self.conn.execute("INSERT INTO CRED (Name,Salt,Pass) VALUES (\"{0}\",\"{1}\",\"{2}\")".format(
                Name, Salt, Pass))
            self.Commit()
        except:
            self.conn.rollback()

    def AddPlugin(self, Name, Description, Version, MainFile, Type):
        try:
            self.conn.execute("INSERT INTO PLUGIN (Name,Description,Version,MainFile,Type) VALUES (\"{0}\",\"{1}\",\"{2}\",\"{3}\",{4})".format(
                Name, Description, Version, MainFile, Type))
            self.Commit()
        except:
            self.conn.rollback()

    def AddRouts(self, ID_Plugin, URI, Type):
        try:
            self.conn.execute("INSERT INTO ROUTS (ID_Plugin,URI,Type) VALUES ({0}, \"{1}\", {2})".format(
                ID_Plugin, URI, Type))
            self.Commit()
        except:
            self.conn.rollback()

    def AddSH_FILES(self, URI_Name, URI_File, UAID):
        try:
            self.conn.execute("INSERT INTO SH_FILES (URI_Name,URI_File,UAID) VALUES (\"{0}\", \"{1}\",{2})".format(
                URI_Name, URI_File, UAID))
            self.Commit()
        except:
            self.conn.rollback()

    def AddTOKEN(self, Hash, Name, CreatTime, EndTime, Description, AccessCode, PluginID, UAID):
        try:
            self.conn.execute("INSERT INTO TOKEN (Hash,Name,CreatTime,EndTime,Description,AccessCode,PluginID,UAID) VALUES (\"{0}\",\"{1}\",{2},{3},\"{4}\",\"{5}\",{6},{7})".format(
                Hash, Name, CreatTime, EndTime, Description, AccessCode, PluginID, UAID))
            self.Commit()
        except:
            self.conn.rollback()

    def AddHOOK(self, SID, Hook, DID, Status, UAID):
        try:
            self.conn.execute("INSERT INTO HOOK (SID,Hook,DID,Status,UAID) VALUES ({0},\"{1}\",{2},{3},{4})".format(
                SID, Hook, DID, Status, UAID))
            self.Commit()
        except:
            self.conn.rollback()

    def AddLOG(self, PluginID, Log, priority, UAID):
        try:
            TimeStamp = time.time()
            self.conn.execute("INSERT INTO LOG (PluginID,Log,TimeStamp,priority) VALUES ({0},\"{1}\",{2},{3},{4})".format(
                PluginID, Log, TimeStamp, priority, UAID))
            self.Commit()
        except:
            self.conn.rollback()

    def AddACCESS(self, PID, UID):
        try:
            self.conn.execute("INSERT INTO ACCESS (PID,UID) VALUES ({0},{1})".format(
                PID, UID))
            self.Commit()
        except:
            self.conn.rollback()

    # removing from table

    def RemovePlugin(self, ID):
        try:
            self.conn.execute("DELETE from PLUGIN where ID={0}".format(ID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveRouts(self, ID):
        try:
            self.conn.execute(
                "DELETE from ROUTS where ID_Plugin={0}".format(ID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveSH_FILES(self, ID):
        try:
            self.conn.execute("DELETE from SH_FILES where ID={0}".format(ID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveTOKEN(self, hash):
        try:
            self.conn.execute(
                "DELETE from TOKEN where Hash=\"{0}\"".format(hash))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveTOKENByEndTime(self, EndTime):
        try:
            self.conn.execute(
                "DELETE from TOKEN where EndTime={0}".format(EndTime))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveHOOKBySID(self, SID):
        try:
            self.conn.execute("DELETE from HOOK where SID={0}".format(SID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveHOOKByDID(self, DID):
        try:
            self.conn.execute("DELETE from HOOK where DID={0}".format(DID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveACCESSByPIDandUID(self, PID, UID):
        try:
            self.conn.execute(
                "DELETE from ACCESS where PID={0} and UID={1}".format(PID, UID))
            self.Commit()
        except:
            self.conn.rollback()

    def lastPluginID(self):
        l = (self.QuarryAllPlugin())[0][-1]
        return (l)

    def ClearLOGs(self):
        try:
            self.conn.execute("Delete from LOG;")
            self.Commit()
        except:
            self.conn.rollback()

    # Update

    def UpdateSH_FILESByID(self, ID, URI_Name, URI_File,UAID):
        try:
            self.conn.execute("UPDATE SH_FILES set URI_Name=\"{0}\", URI_File=\"{1}\",UAID={2} where ID={3}".format(
                URI_Name, URI_File, UAID, ID))
            self.Commit()
        except:
            self.conn.rollback()

    # Misc

    def SqlQuarryExec(self, quarry):
        c = self.conn.cursor()
        c.execute(quarry)
        return (c.fetchall())

    def Commit(self):
        self.conn.commit()

    # def DropTable(self, table):
    #     stm = "DROP TABLE {0};".format(table)
    #     self.SqlQuarryExec(stm)
    #     self.Commit()


if __name__ == "__main__":
    db = DB_Manager()
    db.TableCreation()
    db.AddSH_FILES("Home", "index.html", 1)
    db.AddSH_FILES("Login", "login.html", 1)
    db.AddSH_FILES("Register", "register.html", 1)
    db.AddSH_FILES("install plugin", "install_plugin.html", 1)
    db.AddSH_FILES("join admin", "join_admin.html", 1)
