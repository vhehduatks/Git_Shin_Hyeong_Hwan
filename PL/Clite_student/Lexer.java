package PL.Clite_student;
import java.io.*;

public class Lexer {

    private boolean isEof = false;
    private char ch = ' '; 
    private BufferedReader input;
    private String line = "";
    private int lineno = 0;
    private int col = 1;
    private final String letters = "abcdefghijklmnopqrstuvwxyz"
        + "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private final String digits = "0123456789";
    private final char eolnCh = '\n';
    private final char eofCh = '\004';
    

    public Lexer (String fileName) { // source filename
        try {
            input = new BufferedReader (new FileReader(fileName));
        }
        catch (FileNotFoundException e) {
            System.out.println("File not found: " + fileName);
            System.exit(1);
        }
    }

    private char nextChar() { // Return next char
        if (ch == eofCh)    //현제 가지고있는 ch가 파일의 끝일경우
            error("Attempt to read past end of file");
        col++;  //파일의 끝이 아닐경우 다음 문자열의 idx를 가르킴
        if (col >= line.length()) { //idx가 라인의 길이를 초과할경우=라인을 다 읽었을경우 (처음의 값은 각각 line="",ch=' ',col=1이다)
            try {
                line = input.readLine();    //새로운 라인을 하나 읽어온다
            } catch (IOException e) {
                System.err.println(e);
                System.exit(1);
            } // try
            if (line == null) // at end of file 새로운 라인이 없을경우에
                line = "" + eofCh;//파일의 끝(eof)을 라인에 붙임
            else {//새로운 라인이 존재할 경우엔
                System.out.println(lineno + ": " + line);//라인 넘버와 라인을 출력
                lineno++;//라인 넘버를 +1하고
                line += eolnCh;//읽어온 라인의 끝에 eol을 붙여서 한 줄로 만든다.
            } // if line
            col = 0;//라인을 새로 읽어왔으니 라인의 idx를 0으로 초기화한다.
        } // if col
        return line.charAt(col);//라인의 문자 하나씩을 리턴한다.
    }
            

    public Token next( ) { // Return next token
        do {
            if (isLetter(ch)) { // ident or keyword 읽어온 문자가 알파뱃이면
                String spelling = concat(letters + digits); // 문자들을 토큰으로 만들어서 
                return Token.keyword(spelling); //글자 토큰리턴
            } else if (isDigit(ch)) { // int or float literal
                String number = concat(digits);
                if (ch != '.')  // int Literal
                    return Token.mkIntLiteral(number);
                number += concat(digits);
                return Token.mkFloatLiteral(number);
            } else switch (ch) { //ch가 숫자도 아니고 글자도 아닐 경우
            case ' ':   // 공백
            case '\t':  //탭
            case '\r':  //개행 문자 (커서를 행의 앞으로 이동시킴)
            case eolnCh:    //개행문자 라인 피드 \n
                ch = nextChar(); //위의 4가지 경우일때 ch에 다음 문자를 저장하고 
                break;//루프를 탈출=하나의 토큰임.
            
            case '/':  // divide or comment 나누기 or 주석
                ch = nextChar(); //다음 문자를 가져옴
                if (ch != '/')  // '/'이 한번 나올 경우
                    return Token.divideTok; //나누기 토큰을 리턴
                // '/'가 두번 나올 경우
                do {
                    ch = nextChar();
                } while (ch != eolnCh);//주석이므로 라인의 끝까지 가져옴
                ch = nextChar();//다음 라인의 첫문자를 ch에 저장하고
                break;//탈출
            
            case '\'':  // char literal
                char ch1 = nextChar();
                nextChar(); // get '
                ch = nextChar();
                return Token.mkCharLiteral("" + ch1);
                
            case eofCh: 
                return Token.eofTok;
            
            case '+': 
                ch = nextChar();
                return Token.plusTok;

            // - * ( ) { } ; ,  student exercise
            //------------------------------------------
            case '-':
                ch = nextChar();
                return Token.minusTok;

            case '*':
                ch = nextChar();
                return Token.multiplyTok;

            case '(':
                ch = nextChar();
                return Token.leftParenTok;

            case ')':
                ch = nextChar();
                return Token.rightParenTok;

            case '{':
                ch = nextChar();
                return Token.leftBraceTok;

            case '}':
                ch = nextChar();
                return Token.rightBraceTok;

            case ';':
                ch = nextChar();
                return Token.semicolonTok;
            case ',': ch = nextChar();
                return Token.commaTok;
            //------------------------------------------
                
            case '&': 
                check('&'); 
                return Token.andTok;

            case '|': 
                check('|');
                return Token.orTok;

            case '=':
                return chkOpt('=', Token.assignTok,Token.eqeqTok);
            // < > !  student exercise 
            //------------------------------------------
            case '<':
            return chkOpt('=', Token.ltTok,Token.lteqTok);

            case '>':
            return chkOpt('=', Token.gtTok,Token.gteqTok);

            case '!':
            return chkOpt('=', Token.notTok,Token.noteqTok);
            //------------------------------------------
            default:  error("Illegal character " + ch); 
            } // switch
        } while (true);
    } // next


    private boolean isLetter(char c) {
        return (c>='a' && c<='z' || c>='A' && c<='Z');
    }
  
    private boolean isDigit(char c) {
        return (c>='0' && c<='9');  // student exercise
    }

    private void check(char c) {
        ch = nextChar();
        if (ch != c) 
            error("Illegal character, expecting " + c);
        ch = nextChar();
    }

    private Token chkOpt(char c, Token one, Token two) {//=인지 ==인지 구분 chkOpt('=', Token.assignTok,Token.eqeqTok);
        // student exercise------------------------------
        ch=nextChar();
        if (ch!=c)//ch가 c가 아닌경우 (c는 보통 '=')
            return one;
        ch=nextChar();//이어서'='가 붙은 경우엔 ch를 다음문자로 이동시켜줘야됨 
        return two; 
        // ----------------------------------------------
    }

    private String concat(String set) {
        String r = "";
        do {
            r += ch;
            ch = nextChar();
        } while (set.indexOf(ch) >= 0);
        return r;
    }

    public void error (String msg) {
        System.err.print(line);
        System.err.println("Error: column " + col + " " + msg);
        System.exit(1);
    }

    static public void main ( String[] argv ) {
        Lexer lexer = new Lexer(argv[0]);
        Token tok = lexer.next( );
        while (tok != Token.eofTok) {
            System.out.println(tok.toString());
            tok = lexer.next( );
        } 
    } // main

}

