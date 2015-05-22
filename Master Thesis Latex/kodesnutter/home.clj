(defn home-page []
  (let [view (:view @state)]
    [:div.container
     ..
     (case view
       :kitchen (kitchen " zoom")
       :bathroom (bathroom " zoom")
       :bedroom (bedroom " zoom")
       :garage (garage " zoom")
       :hall (hall " zoom")
       :food (food)
       :weather (weather)
       :diagnostics (diagnostics)
       :home ..
       )]))