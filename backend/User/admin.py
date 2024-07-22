from django.contrib import admin
from .models import User

    # def display_graph(self,obj):
    #     fig, ax = plt.subplots()
    #     ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    #     ax.set_title('Simple plot')
    #     ax.set_xlabel('X-axis')
    #     ax.set_ylabel('Y-axis')
    #     buffer = BytesIO()
    #     # plt.savefig(buffer, format='png')
    #     # buffer = BytesIO()
    #     plt.savefig(buffer, format='png')
    #     buffer.seek(0)
    #     image_base64 = base64.b64encode(buffer.getvalue()).decode()
        
    #     # plt.imshow(buffer.getvalue(), aspect='auto')

    #     plt.close()
    #     return f'<img src="data:image/png;base64,{image_base64}" width="400px" />'
        # return graph

        

# admin.site.register(User,userAdmin)
admin.site.register(User)