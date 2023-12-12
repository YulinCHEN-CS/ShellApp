// Generated from /Users/stephchen/VisualStudioProgram/COMP0010/comp0010-shell-python-p46/src/antlr/ShellGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ShellGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PIPE=1, SEMICOLON=2, STRING=3, ID=4, WS=5;
	public static final int
		RULE_command = 0, RULE_call = 1, RULE_pipe = 2, RULE_seq = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"command", "call", "pipe", "seq"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'|'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PIPE", "SEMICOLON", "STRING", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ShellGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ShellGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public SeqContext seq() {
			return getRuleContext(SeqContext.class,0);
		}
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_command);
		try {
			setState(11);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(8);
				seq();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(9);
				call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(10);
				pipe();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallContext extends ParserRuleContext {
		public Token appName;
		public Token args;
		public List<TerminalNode> ID() { return getTokens(ShellGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ShellGrammarParser.ID, i);
		}
		public List<TerminalNode> STRING() { return getTokens(ShellGrammarParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(ShellGrammarParser.STRING, i);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			((CallContext)_localctx).appName = match(ID);
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==STRING || _la==ID) {
				{
				{
				setState(14);
				((CallContext)_localctx).args = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==STRING || _la==ID) ) {
					((CallContext)_localctx).args = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(19);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipeContext extends ParserRuleContext {
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public List<TerminalNode> PIPE() { return getTokens(ShellGrammarParser.PIPE); }
		public TerminalNode PIPE(int i) {
			return getToken(ShellGrammarParser.PIPE, i);
		}
		public PipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipe; }
	}

	public final PipeContext pipe() throws RecognitionException {
		PipeContext _localctx = new PipeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_pipe);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			call();
			setState(23); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(21);
				match(PIPE);
				setState(22);
				call();
				}
				}
				setState(25); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PIPE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SeqContext extends ParserRuleContext {
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(ShellGrammarParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(ShellGrammarParser.SEMICOLON, i);
		}
		public SeqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seq; }
	}

	public final SeqContext seq() throws RecognitionException {
		SeqContext _localctx = new SeqContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_seq);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			call();
			setState(30); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				match(SEMICOLON);
				setState(29);
				call();
				}
				}
				setState(32); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==SEMICOLON );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0005#\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0003\u0000\f\b\u0000\u0001\u0001\u0001\u0001\u0005\u0001\u0010"+
		"\b\u0001\n\u0001\f\u0001\u0013\t\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0004\u0002\u0018\b\u0002\u000b\u0002\f\u0002\u0019\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0004\u0003\u001f\b\u0003\u000b\u0003\f\u0003 \u0001"+
		"\u0003\u0000\u0000\u0004\u0000\u0002\u0004\u0006\u0000\u0001\u0001\u0000"+
		"\u0003\u0004#\u0000\u000b\u0001\u0000\u0000\u0000\u0002\r\u0001\u0000"+
		"\u0000\u0000\u0004\u0014\u0001\u0000\u0000\u0000\u0006\u001b\u0001\u0000"+
		"\u0000\u0000\b\f\u0003\u0006\u0003\u0000\t\f\u0003\u0002\u0001\u0000\n"+
		"\f\u0003\u0004\u0002\u0000\u000b\b\u0001\u0000\u0000\u0000\u000b\t\u0001"+
		"\u0000\u0000\u0000\u000b\n\u0001\u0000\u0000\u0000\f\u0001\u0001\u0000"+
		"\u0000\u0000\r\u0011\u0005\u0004\u0000\u0000\u000e\u0010\u0007\u0000\u0000"+
		"\u0000\u000f\u000e\u0001\u0000\u0000\u0000\u0010\u0013\u0001\u0000\u0000"+
		"\u0000\u0011\u000f\u0001\u0000\u0000\u0000\u0011\u0012\u0001\u0000\u0000"+
		"\u0000\u0012\u0003\u0001\u0000\u0000\u0000\u0013\u0011\u0001\u0000\u0000"+
		"\u0000\u0014\u0017\u0003\u0002\u0001\u0000\u0015\u0016\u0005\u0001\u0000"+
		"\u0000\u0016\u0018\u0003\u0002\u0001\u0000\u0017\u0015\u0001\u0000\u0000"+
		"\u0000\u0018\u0019\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000"+
		"\u0000\u0019\u001a\u0001\u0000\u0000\u0000\u001a\u0005\u0001\u0000\u0000"+
		"\u0000\u001b\u001e\u0003\u0002\u0001\u0000\u001c\u001d\u0005\u0002\u0000"+
		"\u0000\u001d\u001f\u0003\u0002\u0001\u0000\u001e\u001c\u0001\u0000\u0000"+
		"\u0000\u001f \u0001\u0000\u0000\u0000 \u001e\u0001\u0000\u0000\u0000 "+
		"!\u0001\u0000\u0000\u0000!\u0007\u0001\u0000\u0000\u0000\u0004\u000b\u0011"+
		"\u0019 ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}