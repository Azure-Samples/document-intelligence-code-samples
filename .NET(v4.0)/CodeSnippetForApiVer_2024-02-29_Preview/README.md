- To be consistent style with the Document Intelligence Studio C# sample code snippets, these C# sample use the Top-Level Statement, then it will be convenient to port code. 

- The C# compiler only allows one compilation unit to have top-level statements. So use the preprocessor symbol to control the code scope to facilitate debugging.

- The default sample is "Document analysis\Read.cs", if want to debug other sample, just uncomment the RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT symbol in the file which want to enable, like below:
				      #define RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT
      #if RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT

      *C# sample code with top-level statement*
      ......

      #endif

  and disable other sample codes by commenting out the RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT symbol in other sample files, like below:

      //#define RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT
      #if RUN_AS_ENTRY_OF_TOP_LEVEL_STATEMENT

      *C# sample code with top-level statement*
       ......

      #endif

- If try to port the code, ignore the preprocessor and just take the code part please.