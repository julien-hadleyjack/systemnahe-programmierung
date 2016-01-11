@default_files = ("systemnahe-programmierung.tex");

$pdf_mode = 1;
$dvi_mode = 0;
$ps_mode = 0;

$recorder = 1;

$bibtex_use = 2; # remove .bbl from output on clean
# remove all temporary files which are not removed automatically from output on clean
@generated_exts = qw(fls lof lot toc glg glo gls ist lol run.xml synctex.gz out pyg aux fls);

add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');

sub run_makeglossaries {
  my ($base_name, $path) = fileparse( $_[0] );
  pushd $path;
  my $return = system "makeglossaries $base_name";
  popd;
  return $return;
}

$pdflatex = 'pdflatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 %O %S';
