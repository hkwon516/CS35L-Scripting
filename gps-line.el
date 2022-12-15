:
(defun gps-line ()
  "Print the current buffer line number and narrowed line number of point."
  (interactive)
  (let ((start (point-min))
        (end (point-max))
        (n (line-number-at-pos))
        (total (count-lines (point-min) (point-max))))
    (if (= (point-min) (point-max)) 
        (message "Line %d/%d" 0 0)
    (if (not (= (char-before (point-max)) 10))
          (message "Line %d/%d" n (- total 1))
          (message "Line %d/%d" n total)))))



;if ends in newline count-lines returns OK
;if not end in newline return + 1
; if last char is not new line return -1


;if ends in newline count-lines returns OK
;if not end in newline return + 1
; if last char is not new line return -1
;(narrow-to-region 5 10)
; (point-min 5)

;(line-number-at-pos)
;(widen) -> brings back everything

; if point min == 1 -> no narrowing 
; else then narrow 
; save-restriction - change scope and then turn back to widen/or narrow and get function 
; point-min -> 5 
; line-number-at-pos - doesn't know if narrowed


