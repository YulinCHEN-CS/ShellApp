// Generated from /Users/stephchen/VisualStudioProgram/COMP0010/comp0010-shell-python-p46/src/antlr/Shell.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ShellParser}.
 */
public interface ShellListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ShellParser#commandLine}.
	 * @param ctx the parse tree
	 */
	void enterCommandLine(ShellParser.CommandLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#commandLine}.
	 * @param ctx the parse tree
	 */
	void exitCommandLine(ShellParser.CommandLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ShellParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ShellParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ShellParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ShellParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(ShellParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(ShellParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#seq}.
	 * @param ctx the parse tree
	 */
	void enterSeq(ShellParser.SeqContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#seq}.
	 * @param ctx the parse tree
	 */
	void exitSeq(ShellParser.SeqContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ShellParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ShellParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(ShellParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(ShellParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ShellParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ShellParser.ConditionContext ctx);
}