package PL.Clite_student;
import java.util.*;

public class Parser {
    // Recursive descent parser that inputs a C++Lite program and 
    // generates its abstract syntax.  Each method corresponds to
    // a concrete syntax grammar rule, which appears as a comment
    // at the beginning of the method.
  
    Token token;          // current token from the input stream
    Lexer lexer;
  
    public Parser(Lexer ts) { // Open the C++Lite source program
        lexer = ts;                          // as a token stream, and
        token = lexer.next();            // retrieve its first Token
    }
  
    private String match (TokenType t) {
        String value = token.value();
        if (token.type().equals(t))
            token = lexer.next();
        else
            error(t);
        return value;
    }
  
    private void error(TokenType tok) {
        System.err.println("Syntax error1: expecting: " + tok 
                           + "; saw: " + token);
        System.exit(1);
    }
  
    private void error(String tok) {
        System.err.println("Syntax error2: expecting: " + tok 
                           + "; saw: " + token);
        System.exit(1);
    }
  
    public Program program() {
        // Program --> void main ( ) '{' Declarations Statements '}'
        TokenType[ ] header = {TokenType.Int, TokenType.Main,TokenType.LeftParen, TokenType.RightParen};
        for (int i=0; i<header.length; i++){   // bypass "int main ( )"
            match(header[i]);
        }   
        match(TokenType.LeftBrace);// '{'를 확인
        // student exercise
        //-----------------------------
        Declarations Decs=declarations();  //비터미널이므로 declarations()를 불러옴
        Block B = tempgstatements();   //비터미널이므로 statements()를 불러옴
        //-----------------------------
        match(TokenType.RightBrace);// '}'를 확인
        return new Program(Decs,B);  // student exercise
    }
  
    private Declarations declarations () {
        // Declarations --> { Declaration } //{}메타기호 반복
        //-----------------------------
        Declarations Ds = new Declarations();
        while(isType()){
            declaration(Ds);
        }
        return Ds;  // student exercise
        //-----------------------------
    }
  
    private void declaration (Declarations ds) {
        // Declaration  --> Type Identifier { , Identifier } ; //{}메타기호 반복 ','가 있으면 계속 반복
        // student exercise
        //-----------------------------
        Type t=type(); //비터미널이므로 type()를 불러옴
        Variable v = new Variable(match(TokenType.Identifier)); //비터미널
        Declaration d = new Declaration(v, t);  //Declarations 에 추가할 Declaration 객체를 생성
        ds.add(d);  //추가
        while (isComma()) {	//','가 있으면 뒤에  Declaration이 추가로 반복됨
			token = lexer.next();	
			v = new Variable(match(TokenType.Identifier));
			d = new Declaration(v, t);	
			ds.add(d);
		}//while로 메타기호를 처리
	    match(TokenType.Semicolon);//세미콜론 처리
        //-----------------------------
    }
  
    private Type type () {
        // Type  -->  int | bool | float | char 
        Type t = null;
        // student exercise
        //-----------------------------
        if (token.type().equals(TokenType.Int))//토큰의 타입이
            t = Type.INT;//일치하면
        else if (token.type().equals(TokenType.Bool))
            t = Type.BOOL;//해당
        else if (token.type().equals(TokenType.Float))
            t = Type.FLOAT;//타입을
        else if (token.type().equals(TokenType.Char))
            t = Type.CHAR;//t에 저장하고
        // else if (token.type().equals(TokenType.Void))
        //     t = Type.VOID;//저장하고
        else 
            error("int | bool | float | char | void");
        token = lexer.next();//다음 토큰을 token에 불러온 다음
        //-----------------------------
        return t;//타입을 리턴
    }
  
    private Statement statement() { //코드조각?
        // Statement --> ; | Block | Assignment | IfStatement | WhileStatement //선택이므로 else if로 구현
        Statement s = null;
        // student exercise
        //-----------------------------
        if (token.type().equals(TokenType.Semicolon))   //세미콜론일경우
		    s = new Skip(); //넘어감
	    else if (token.type().equals(TokenType.LeftBrace)) //Block일경우(토큰이'{' 이면 블록의 시작)
		    s = statements();   //statements() (블록)을 가져옴(비터미널)
        else if (token.type().equals(TokenType.Identifier)) //Assignment(할당문)일 경우
		    s = assignment();   //assignment() (할당문)을 가져옴(비터미널)
        else if (token.type().equals(TokenType.If)) //if 문일경우
		    s = ifStatement();  //ifStatement() (if문)을 가져옴(비터미널)
	    else if (token.type().equals(TokenType.While)) //while 문일경우
		    s = whileStatement();   //whileStatement() (while문)을 가져옴(비터미널)
	    else 
            error("Error in Statement construction");
        //-----------------------------
        return s;   //가져온 코드조각을 리턴
    }

    //-----------------------------
    // program() 엔 match(TokenType.LeftBrace); 이라는 함수가 있어서 이미 '{'를 통과했음에도 불구하고 statements() 에선 추가로
    //match(TokenType.LeftBrace); 를 확인하는 과정을 거치므로 에러가 발생한다. 따라서 program() 내부의 Block() 에는 '{'와 '}'를 확인하는 match가 없어야 함
    private Block tempgstatements( ) {                                   
	Block b = new Block();
	Statement s;
	while (isStatement()) {
		s = statement();
		b.members.add(s);
	}

        return b;
    }
    //-----------------------------

    private Block statements() {    //블록은 여러 코드조각이 모인것
        // Block --> '{' Statements '}' //메타기호가 아님 그냥 중괄호
        Block b = new Block();
        // student exercise
        //-----------------------------
        Statement s;    //코드조각 객체를 생성
        match(TokenType.LeftBrace); //'{'를 확인

	    while (isStatement()) { //블록 내부의 코드조각이 끝날때까지
		    s = statement();    //코드조각 객체를 생성해서
		    b.members.add(s);   //블록에 추가
	    }

        match(TokenType.RightBrace);// end of the block '}'를 확인
        //-----------------------------
        return b;
    }
  
    private Assignment assignment() {
        // Assignment --> Identifier = Expression ;
        //-----------------------------
        Variable target = new Variable(match(TokenType.Identifier)); //추상화 카테고리 상 Variable 임,Identifier 
        match(TokenType.Assign);    //터미널 '=' 확인
        Expression source = expression();   //비터미널이므로 expression()
        match(TokenType.Semicolon); //터미널 ';' 확인
        return new Assignment(target, source); // student exercise
        //-----------------------------
    }
  
    private Conditional ifStatement() {
        // IfStatement --> if '(' Expression ')' Statement [ else Statement ] //[]는 메타기호
        //-----------------------------
        Conditional c;
    
        match(TokenType.If);    //토큰을
        match(TokenType.LeftParen); //확인
        Expression e = expression();    //비터미널이므로 메소드 가져옴
        match(TokenType.RightParen);    //토큰 확인
        Statement s = statement();      //비터미널
        if (token.type().equals(TokenType.Else)) {  //옵셔널이므로 else가 있으면 코드조각을 이어서 가져오고 else가 없으면 안가져옴
            Statement elses = statement();
            c = new Conditional(e,s,elses); //else가 있을경우 이어지는 코드조각을 conditional 객체에 추가
        }
        else {
            c = new Conditional(e, s);//else가 없을경우
        }
        return c; // student exercise
        //----------------------------- 
    }
  
    private Loop whileStatement () {
        // WhileStatement --> while '(' Expression ')' Statement
        //-----------------------------
        match(TokenType.While); //터미널
        match(TokenType.LeftParen); //토큰들
        Expression e = expression();    //비터미널
        match(TokenType.RightParen);    //터미널
        Statement s = statement();  //비터미널
        return new Loop(e,s);  // student exercise
        //-----------------------------
    }

    private Expression expression () {
        // Expression --> Conjunction { || Conjunction } //or 구문 메타기호 반복
        //-----------------------------
        Expression c1 = conjunction();
	    while (token.type().equals(TokenType.Or)) { //or토큰이 나오면 반복
		    Operator op = new Operator(match(token.type()));
		    Expression c2 = conjunction();
		    c1 = new Binary(op, c1, c2);
	    }
	    return c1;  // student exercise
        //-----------------------------
    }
  
    private Expression conjunction () {
        // Conjunction --> Equality { && Equality }// and 구문 메타기호 반복
        //-----------------------------
        Expression eq1 = equality();
        while (token.type().equals(TokenType.And)) { //and 토큰이 나오면 반복
            Operator op = new Operator(match(token.type()));
            Expression eq2 = equality();
            eq1 = new Binary(op, eq1, eq2);
        }
        return eq1;  // student exercise
        //-----------------------------
    }
  
    private Expression equality () {
        // Equality --> Relation [ EquOp Relation ] //메타문자 옵셔널
        //-----------------------------
        Expression re1 = relation();
        if (isEqualityOp()) {  //옵셔널이므로 EquOp 가 있으면 코드조각을 이어서 가져오고 EquOp 가 없으면 안가져옴
            Operator op = new Operator(match(token.type()));
            Expression re2 = relation();
            re1 = new Binary(op,re1,re2); 
            return re1;
        }else{
            return re1;//EquOp 가 없을경우
        }
        //-----------------------------
    }

    private Expression relation (){
        // Relation --> Addition [RelOp Addition] //메타문자 옵셔널
        //-----------------------------
        Expression ad1 = addition();
        if (isRelationalOp()) {  //옵셔널이므로 RelOp 가 있으면 코드조각을 이어서 가져오고 RelOp 가 없으면 안가져옴
            Operator op = new Operator(match(token.type()));
            Expression ad2 = addition();
            ad1 = new Binary(op,ad1,ad2); 
            return ad1;
        }else{
            return ad1;//EquOp 가 없을경우
        }
        //-----------------------------
    }
  
    private Expression addition () {
        // Addition --> Term { AddOp Term }
        Expression e = term();
        while (isAddOp()) {
            Operator op = new Operator(match(token.type()));
            Expression term2 = term();
            e = new Binary(op, e, term2);
        }
        return e;
    }
  
    private Expression term () {
        // Term --> Factor { MultiplyOp Factor }
        Expression e = factor();
        while (isMultiplyOp()) {
            Operator op = new Operator(match(token.type()));
            Expression term2 = factor();
            e = new Binary(op, e, term2);
        }
        return e;
    }
  
    private Expression factor() {
        // Factor --> [ UnaryOp ] Primary 
        if (isUnaryOp()) {
            Operator op = new Operator(match(token.type()));
            Expression term = primary();
            return new Unary(op, term);
        }
        else return primary();
    }
  
    private Expression primary () {
        // Primary --> Identifier | Literal | ( Expression )
        //             | Type ( Expression )
        Expression e = null;
        if (token.type().equals(TokenType.Identifier)) {
            e = new Variable(match(TokenType.Identifier));
        } else if (isLiteral()) {
            e = literal();
        } else if (token.type().equals(TokenType.LeftParen)) {
            token = lexer.next();
            e = expression();       
            match(TokenType.RightParen);
        } else if (isType( )) {
            Operator op = new Operator(match(token.type()));
            match(TokenType.LeftParen);
            Expression term = expression();
            match(TokenType.RightParen);
            e = new Unary(op, term);
        } else error("Identifier | Literal | ( | Type");
        return e;
    }

    private Value literal( ) {
        //-----------------------------
        Value value = null;
        String stval = token.value();
        if (token.type().equals(TokenType.IntLiteral)) {
            value = new IntValue (Integer.parseInt(stval));
            token = lexer.next();
        }
        else if (token.type().equals(TokenType.FloatLiteral))  {
            value = new FloatValue(Float.parseFloat(stval));
            token = lexer.next();
        }
        else if (token.type().equals(TokenType.CharLiteral))  {
            value = new CharValue(stval.charAt(0));
            token = lexer.next();
        }
        else if (token.type().equals(TokenType.True))  {
            value = new BoolValue(true);
            token = lexer.next();
        }
        else if (token.type().equals(TokenType.False))  {
            value = new BoolValue(false);
            token = lexer.next();
        }
        else 
            error ("Error in literal value contruction");
        return value;
        //-----------------------------
    }
    
  

    private boolean isAddOp( ) {
        return token.type().equals(TokenType.Plus) ||
               token.type().equals(TokenType.Minus);
    }
    
    private boolean isMultiplyOp( ) {
        return token.type().equals(TokenType.Multiply) ||
               token.type().equals(TokenType.Divide);
    }
    
    private boolean isUnaryOp( ) {
        return token.type().equals(TokenType.Not) ||
               token.type().equals(TokenType.Minus);
    }
    
    private boolean isEqualityOp( ) {
        return token.type().equals(TokenType.Equals) ||
            token.type().equals(TokenType.NotEqual);
    }
    
    private boolean isRelationalOp( ) {
        return token.type().equals(TokenType.Less) ||
               token.type().equals(TokenType.LessEqual) || 
               token.type().equals(TokenType.Greater) ||
               token.type().equals(TokenType.GreaterEqual);
    }
    
    private boolean isType( ) {
        return token.type().equals(TokenType.Int)
            || token.type().equals(TokenType.Bool) 
            || token.type().equals(TokenType.Float)
            || token.type().equals(TokenType.Char);
    }
    
    private boolean isLiteral( ) {
        return token.type().equals(TokenType.IntLiteral) ||
            isBooleanLiteral() ||
            token.type().equals(TokenType.FloatLiteral) ||
            token.type().equals(TokenType.CharLiteral);
    }
    
    private boolean isBooleanLiteral( ) {
        return token.type().equals(TokenType.True) ||
            token.type().equals(TokenType.False);
    }
    //-----------------------------
    private boolean isLeftBrace() {
        return token.type().equals(TokenType.LeftBrace);
    } 

    private boolean isSemicolon( ) {
        return token.type().equals(TokenType.Semicolon);
    }

    private boolean isStatement() {
        return 	isSemicolon() || isLeftBrace() || token.type().equals(TokenType.If) || token.type().equals(TokenType.While) || token.type().equals(TokenType.Identifier); 
    }

    private boolean isComma( ) {
        return token.type().equals(TokenType.Comma);
    }

    
    //-----------------------------
    public static void main(String[] args) {
        System.out.println(args[0]);
        Parser parser  = new Parser(new Lexer(args[0]));
        Program prog = parser.program();
        System.out.println(prog);
        prog.display(1);           // display abstract syntax tree
    } //main

} // Parser
