class PasswordConstants:
    SALT="salt"
    HASHED_PASSWORD="hashed_password"
    LENGTH=10


class CommonConstants:
    EMAIL="email"
    PHONE="phone"
    PASSWORD="password"
    USER_AGENT="user_agent"
    VERIFIED="verified"
    USER_ID="user_id"
    ROLE="role"
    ID="id"
    INBOX_ID="inbox_id"
    COLLEGE_PREFIX="3490"
    CLASS_OF_STUDENT="classofstudent"
    FNAME="fname"
    MNAME="mname"
    LNAME="lname"
    DEPT="dept"
    ROLE="role"
    CLASS="class"
    ACCESS_LEVEL="access_level"
    SESSION_ID="session_id"
    LAST_UPDATED_TIME="last_updated_time"
    DOB="dob"
    CLIENT_IP="client_ip"


class SqlDBConstants :
    pass

class TypeClassifications:
    DEPTCODE={"EE":"16","CS":"11"}
    USERROLE={"1":"SD","2":"TH","3":"ST", "4":"SF"}

    #SD = Super Admin
    #ST = Student
    #SF = Staff
    #TH = Teacher

class SessionConstants:
    PHONE_LOGIN="phone_login"