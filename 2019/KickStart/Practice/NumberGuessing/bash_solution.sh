read t
for p in $(seq 1 $t); do
  read -a line
  a=${line[0]}
  b=${line[1]}
  read n
  head=$(( a+1 ))
  tail=$b
  while true; do
    mid=$(( (head+tail)/2 ))
    echo $mid
    read s
    if [[ "$s" == "CORRECT" ]]; then
      break
    elif [[ "$s" == "TOO_BIG" ]]; then
      tail=$(( mid - 1 ))
    elif [[ "$s" == "TOO_SMALL" ]]; then
      head=$(( mid + 1 ))
    else
      # Wrong answer; exit to receive Wrong Answer judgment
      exit 0
    fi
  done
done