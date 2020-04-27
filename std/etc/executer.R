
#Perform all R commands
main_wrapper_R <- function() {
    source("program.R")
}

#If there is any problem, the script will be stopped
tryCatch(main_wrapper_R(),
    error = function(m) {
        library("tools")
        pskill(Sys.getpid(), signal=SIGKILL)
    }
)
