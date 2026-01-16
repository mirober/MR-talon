app: mintty.exe
app: windowsterminal.exe
app: WindowsTerminal.exe
app: /.*/
and title: /MSYS:.*/

app: Visual Studio Code
and user.vs_terminal: True
-
tag(): user.terminal
tag(): user.command_mode
tag(): user.kubectl
(CD | C D | see dee) {user.directories}:
    insert('cd "{directories}" && ls')
    key(enter)
file {user.files}:
    insert('{files} ')
folder {user.directories}:
    insert('{directories}/')
go {user.folders}:
    "cd {folders} && ls"
    key(enter)
dot {user.extensions}:
    ".{extensions}"
maker {user.makefile_targets}:
    "make {makefile_targets}"
#------------------------------------------------------
change mod: "chmod "
change mod (ex | executable): "chmod +x "
base sixty four: "base64 "
base sixty four decode: "base64 -d "
sudo apt install: "sudo apt install "
bash: "bash "
cancel: key(ctrl-c)
history: key(ctrl-r)
files: key(ctrl-t)
page forward: key(ctrl-s)
see dee up:
    "cd .."
    key(enter)
(CD | C D | see dee): "cd "
curly: "curl "
greppy: "egrep "
greppy recursive: "egrep -R "
header: "head "
echo: "echo "
list: "ls "
long list: "ls -lah "
remove: "rm "
remove recursive: "rm -rf "
line count: "wc -l "
make directory: "mkdir "
move file: "mv "
lodge and: " && "
to file: " > "
sed replace:
    'sed -i -e "s///g"'
    key(left:4)
sumatra [PDF]: "SumatraPDF "
jupiter notebook: "jupyter notebook"
jupiter lab: "jupyter lab"
youtube download: "youtube-dl -f best "
FFM peg: "ffmpeg "
W get: "wget "
catty: "cat "
explorer here:
    "explorer ."
    key(enter)
code here:
    "code ."
    key(enter)
#------------------------------------------------------
# options
option continue: " --continue "
option abort: " --abort "
option skip: " --skip "
option help: " --help"
option version: " --version"
option {user.alphabet}: " -{alphabet} "
#------------------------------------------------------
PDF LaTeX: "pdflatex "
bib TeX: "bibtex "
pan doc:
    'pandoc  -o '
    key(left:4)
pan doc beamer:
    "pandoc  -t beamer -o "
    key(left:14)
#------------------------------------------------------
# python
python: "python "
python debug: "python -m pdb -c c "
python pytest: "python -m pytest "
pip install: "pip install "
pip install requirements: "pip install -r requirements.txt "
pip install editable: "pip install -e ."
upgrade pip: "--upgrade pip"
pie test: "pytest  "
pie test debug: "pytest --pdb "
pie flakes: "pyflakes "
eye python: "ipython "
venv activate: "activate"
venv deactivate: "deactivate"
you've sink: "uv sync "
you've run: "uv run "
#------------------------------------------------------
# r
R script:
    "Rscript .r"
    key(left:2)
R markdown:
    "Rscript -e \"rmarkdown::render('.Rmd', clean=TRUE)\""
    key(left:19)
#------------------------------------------------------
# image
image [magic] trim:
    "convert  -fuzz 1% -trim +repage "
    key(left:24)
image [magic] transparent:
    "convert  -fuzz 1% -transparent white "
    key(left:29)
rename PNG large: "rename 'png_large' 'png' *.png_large"
rename jay peg large: "rename 'jpg_large' 'jpg' *.jpg_large"
# ------------------------------------------------
mux attach: "tmux att"
mux new: key(ctrl-b c)
mux detach: key(ctrl-b d)
mux next: key(ctrl-b n)
mux previous: key(ctrl-b p)
mux find: key(ctrl-b f)
mux close: key(ctrl-b x)
mux step: key(ctrl-b b)
mux split: key(ctrl-b %)
mux split (horizontal | down): key(ctrl-b ")
mux swap: key(ctrl-b o)
mux numbers: key(ctrl-b q)
mux kill: key(ctrl-b x)
mux layout: key(ctrl-b space)
mux page up: key(ctrl-b pgup)
mux (big) down [<user.n20>]: key("ctrl-b ctrl-down:{n20 or 1}")
mux (big) left [<user.n20>]: key("ctrl-b ctrl-left:{n20 or 1}")
mux (big) right [<user.n20>]: key("ctrl-b ctrl-right:{n20 or 1}")
mux (big) up [<user.n20>]: key("ctrl-b ctrl-up:{n20 or 1}")


complete: key(alt-?)
# ------------------------------------------------
go build: "go build "
go clean: "go clean "
go doc: "go doc "
go env: "go env "
go fix: "go fix "
go format: "go fmt "
go generate: "go generate "
go get: "go get "
go install: "go install "
go list: "go list "
go mod: "go mod "
go mod init: "go mod init "
go mod tidy: "go mod tidy "
go work: "go work "
go run: "go run "
go test: "go test "
go tool: "go tool "
go version: "go version "
go vet: "go vet "
go lint: "golangci-lint run\n"
go style: "golangci-lint run  -E stylecheck -e ST1000:\n"
run config check: "configcheck\n"

previous <number>: key("alt:down {number} . alt:up")

ruff check: "ruff check "
ruff check fix: "ruff check --fix "
ruff format: "ruff format "

cloud sequel proxy: "cloud-sql-proxy "

pilot suggest [<phrase>]:
    "gh copilot suggest '{phrase or ''}'"
    key(left)
