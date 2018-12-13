import matplotlib.pyplot as plt

class view:

    def __init__(self):
       pass

    def draw(self, original_df, current_df, img):

        print("im in draw")
        table = current_df.groupby(['filename', 'obj']).size().head(200)
        df_by_obj = original_df.set_index(['filename', 'obj']).sort_index()

        plt.imshow(img)

        for t in table.index:
            s_o = df_by_obj.loc[t]
            s_o.sort_values('seq')
            plt.plot(s_o.x, s_o.y, label = t[1])
        plt.legend(loc=9, bbox_to_anchor=(1.1, 1))

        # plt.show(block=False)

        plt.pause(0.5)
        plt.gcf().clear()

    def draw_one_by_one(self, original_df, current_df, img):

        print("im in draw_one_by_one")

        table = current_df.groupby(['filename', 'obj']).size()
        df_by_obj = original_df.set_index(['filename', 'obj']).sort_index()

        for t in table.index:
            s_o = df_by_obj.loc[t]
            s_o.sort_values('seq')
            plt.imshow(img)
            plt.plot(s_o.x, s_o.y, label=t[1])
            plt.legend(loc=9, bbox_to_anchor=(1.1, 1))
            # plt.show(block=False)
            plt.pause(0.5)
            plt.gcf().clear()
            next = input("next?: ")
            if next != 'y':
                break
