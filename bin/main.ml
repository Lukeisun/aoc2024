let read_input filename =
  let rec read channel =
    try
      let line = input_line channel in
      line :: read channel
    with End_of_file ->
      close_in channel;
      []
  in
  read (open_in (String.concat "" [ "inputs/"; filename ]))

let day1 () =
  let rec read channel =
    try
      let line = input_line channel in
      let split =
        List.map
          (fun element -> int_of_string element)
          (Str.split (Str.regexp "   ") line)
      in
      split :: read channel
    with End_of_file ->
      close_in channel;
      []
  in
  let channel = open_in "inputs/day01.in" in
  let slist = read channel in
  let left = List.map (fun lst -> List.nth lst 0) slist in
  let right = List.map (fun lst -> List.nth lst 1) slist in
  let sleft = List.sort (fun a b -> a - b) left in
  let sright = List.sort (fun a b -> a - b) right in
  let t =
    List.fold_left ( + ) 0 (List.map2 (fun a b -> abs (a - b)) sleft sright)
  in
  print_int t;
  print_newline ();
  let count_unique list =
    let tbl = Hashtbl.create (List.length left) in
    let update x =
      if Hashtbl.mem tbl x then
        let curr = Hashtbl.find tbl x in
        Hashtbl.replace tbl x (succ curr)
      else Hashtbl.replace tbl x 1
    in
    List.iter update list;
    tbl
  in
  let rmap = count_unique right in
  let find_rmap x =
    match Hashtbl.find_opt rmap x with Some value -> value | None -> 0
  in
  let p2 = List.fold_left ( + ) 0 (List.map (fun a -> a * find_rmap a) sleft) in
  print_int p2;
  print_newline ();
  ()

let day2 () = ()

let () =
  let day =
    match Array.to_list Sys.argv with
    | _ :: day :: _ -> int_of_string day
    | _ -> 1
  in
  match day with 1 -> day1 () | 2 -> day2 () | _ -> print_endline "Not impld"
