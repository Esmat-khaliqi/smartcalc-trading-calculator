class Trade():
    def __init__(self,ui):
        self.ui = ui


    # trade Button Calculator    
        self.trade_calcula_btn = self.ui.trade_calculat_btn
        self.trade_calcula_btn.clicked.connect(self.trade_calculat_btn_action)
    # start get btn for clicked 
        self.acc_balance = self.ui.acc_b
        self.entry_price = self.ui.entry_p
        self.take_profit = self.ui.tp
        self.risk = self.ui.risk_percent
        self.stop_loss = self.ui.sl
        self.risk_reward_ratio = self.ui.risk_reward_r

    # start get widgets for add values
        self.info_error =  self.ui.info_label

        self.risk_A_label = self.ui.risk_A_label
        self.pot_Loss_label = self.ui.pot_Loss_label
        self.rr_label = self.ui.rr_label
        self.pot_Size_label = self.ui.pot_Size_label
        self.pot_Profit_label = self.ui.pot_Profit_label
        self.pot_SLD_label = self.ui.pot_SLD_label

        self.TP_label = self.ui.TP_label
        self.Entry_label = self.ui.Entry_label
        self.Stop_loss_label = self.ui.Stop_loss_label

        self.result_frame = self.ui.result_frame




    def trade_calculat_btn_action(self):
        if not all([
            self.acc_balance.text(),
            self.risk.text(),
            self.entry_price.text(),
            self.stop_loss.text()
        ]):
            self.info_error.setText('Missing Required Inputs')
            return
        try:
            # 2. Get input values
            balance = float(self.acc_balance.text())
            risk = float(self.risk.text())
            entry = float(self.entry_price.text())
            sl = float(self.stop_loss.text())


            if balance <= 0 or risk <= 0 or risk > 100:
                self.info_error.setText("Invalid Balance or Risk")
                return

            if entry <= 0 or sl <= 0 or entry == sl:
                self.info_error.setText("Invalid Entry or Stop Loss")
                return

            result_risk_A = balance * risk / 100

            if sl < entry:
                trade_type = "LONG"
                result_stop_distance = entry - sl

            else:
                trade_type = "SHORT"
                result_stop_distance = sl - entry


            tp_text = self.take_profit.text()
            rr_text = self.risk_reward_ratio.text()

            if tp_text:

                tp = float(tp_text)

                if tp <= 0:
                    self.info_error.setText("Invalid Take Profit")
                    return

                if trade_type == "LONG" and tp > entry:
                    result_reward_distance = tp - entry

                elif trade_type == "SHORT" and tp < entry:
                    result_reward_distance = entry - tp

                else:
                    self.info_error.setText("Invalid Take Profit Direction")
                    return

            elif rr_text:

                rr = float(rr_text)

                if rr <= 0:
                    self.info_error.setText("Invalid Risk Reward")
                    return

                result_reward_distance = result_stop_distance * rr

                if trade_type == "LONG":
                    tp = entry + result_reward_distance

                else:
                    tp = entry - result_reward_distance

            else:
                self.info_error.setText("Enter Take Profit or Risk Reward")
                return


            result_position_size = result_risk_A / result_stop_distance


            result_potential_loss = (
                result_position_size * result_stop_distance
            )

            result_potential_profit = (
                result_position_size * result_reward_distance
            )

            result_risk_reward_ratio = (
                result_reward_distance / result_stop_distance
            )

  
            self.risk_A_label.setText(f"${result_risk_A:g}")
            self.pot_SLD_label.setText(f"{result_stop_distance:g}")
            self.pot_Size_label.setText(f"{result_position_size:g} units")
            self.pot_Loss_label.setText(f"${result_potential_loss:g}")
            self.pot_Profit_label.setText(f"${result_potential_profit:g}")
            self.rr_label.setText(f"{result_risk_reward_ratio:g} : {risk:g}")
            self.TP_label.setText(f"${tp:g}")
            self.Entry_label.setText(f"${entry:g}")
            self.Stop_loss_label.setText(f"${sl:g}")

            self.ui.trading_pages.setCurrentWidget(self.result_frame)
        except ValueError:
            self.info_error.setText("Please Enter Valid Numbers")


