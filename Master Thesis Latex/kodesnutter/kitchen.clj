(defn kitchen [z]
  [:div {:className (str "room" z (when (:lights-off? (:livingroom (:rooms @state))) " dark"))}
   [:img.room-image {:src       (:kitchen imgs)
                     :on-click #(swap! state assoc :view :kitchen)}]
   [:img.fridge {:src       (:fridge imgs)
                 :on-click  #(swap! state assoc :view :food)}]
   (if (:active? (:dish-washer (:kitchen (:rooms @state))))
     [:div
      [:img.dish {:src      (:dish-on imgs)
                  :on-click #(swap! state assoc-in [:rooms :kitchen :dish-washer :active?] false)}]]
      [:img.dish {:src      (:dish-off imgs)
                  :on-click #(swap! state assoc-in [:rooms :kitchen :dish-washer :active?] true)}])
    ..
    ])