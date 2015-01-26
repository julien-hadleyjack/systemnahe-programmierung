@REM @ECHO off

CALL activate markdown-latex

ECHO Creating chapter template.
python scripts/apply_template.py template -i "chapters-latex" -t chapter-template.tex "special-generated/chapter-template.tex"

ECHO.
ECHO Converting markdown to LaTeX.
FOR /r %%I in (chapters-markdown\*.md) do pandoc -f markdown --chapters --template special-generated\chapter-template.tex -t latex chapters-markdown\%%~nI.md -o chapters-latex\%%~nI.tex
@REM # Use listings.
@REM # sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' "systemnahe-programmierung"}}.tex
@REM # sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' "systemnahe-programmierung"}}.tex

ECHO Using Jinja on LaTeX directory.
python scripts/apply_template.py transform -i "chapters-latex"
if %errorlevel% neq 0 (
    CALL deactivate
    exit /b %errorlevel%
)

ECHO.
ECHO Using Jinja
python scripts/apply_template.py template -i "chapters-latex" -t overview.tex "systemnahe-programmierung.tex" ^
															  -t customsettings.sty "special-generated/customsettings.sty"


@REM ECHO Transforming images.
@REM python scripts/transform_img_eps.py

ECHO.
ECHO First latex run.
latex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex 1>NUL

ECHO.
ECHO Running bibtex.
bibtex "systemnahe-programmierung"

ECHO.
ECHO Second latex run.
latex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex 1>NUL

ECHO.
ECHO Running pdflatex.
pdflatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex

CALL deactivate

