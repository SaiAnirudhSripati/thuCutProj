from django.shortcuts import render,redirect
from django.http import HttpResponse
from listApp.forms import NewListItemForm
from listApp.models import Categories
from listApp.models import List
from listApp.models import PageVisits
# Create your views here.
def update_page_view_count(pn):
    try:
        page_visits=PageVisits.objects.get(page_name=pn)
    except:
        page_visits=''

    if page_visits:
        page_visits=PageVisits.objects.get(page_name=pn)
        page_vists_viewcount=page_visits.view_count
        page_visits.view_count=page_vists_viewcount+1
        page_visits.save()
    else:
        PageVisits.objects.create(page_name=pn,view_count=1)
    page_visits=PageVisits.objects.get(page_name=pn)
    return page_visits.view_count


def list(request):

    categories=Categories.objects.all()
    view_count=update_page_view_count('home_page')
    return render(request, 'list_cat.html',{'categories': categories,'page_visits':view_count})

def list_items(request,pk):
    list_items=List.objects.filter(cat_id=pk)
    cat_item=Categories.objects.get(id=pk)
    if list_items:
        list_views_count=list_items[0].list_views

        page_visits=list_items[0].list_views
        List.objects.filter(cat_id=pk).update(list_views=list_views_count+1)
    else:
        page_visits=0

    return render(request,'list_items.html',{'lists':list_items,'cat_item':cat_item,'page_visits':page_visits})


def create_item(request,pk):
    category=Categories.objects.get(id=pk)

    if request.method== 'POST':
        form = NewListItemForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.cat_id=pk
            list.save()
            return redirect('list_items', pk=pk)
        else:
            return render(request,'create_item.html',{'cat_id':pk,'cat_name':category.cat_name,'form':form})
            #return HttpResponse("fail")
    else:
        view_count=update_page_view_count('create_item_page')
        form = NewListItemForm()
        #breakpoint()
    return render(request,'create_item.html',{'cat_id':pk,'cat_name':category.cat_name,'form':form,'page_visits':view_count})

def detail(request,pk):

    list_item=List.objects.get(id=pk)
    cat_item=Categories.objects.get(id=list_item.cat_id)
    view_count=update_page_view_count('detail_page')
    return render(request,'detail.html',{'list':list_item,'cat_item':cat_item,'page_visits':view_count})

def delete(request,pk):
    list_item=List.objects.get(id=pk)
    list_item.delete()
    return redirect('list_items', pk=list_item.cat_id)
