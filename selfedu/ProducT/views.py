from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from ProducT.forms import CreationForm
from ProducT.models import Product
from django.views.generic import DetailView

from django.shortcuts import render
from django.http import FileResponse, Http404

def creation_view(request):
    # product = request.product
    context = {}
    if request.POST:
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('main_view')
        else:
            context['creation_form'] = form
    return render(request, 'ProducT/create.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

def main_view(request):
    Products = Product.objects.order_by('date_created')
    return render(request, 'ProducT/Products.html', {'Products': Products})


# def view_pdf(request, pk):
#     pdf = get_object_or_404(Product, pk=pk)
#     image_data = open(pdf.file.url, "rb").read()
#     return HttpResponse(image_data, contenttype='application/pdf')


def detailed_view(request, *args, **kwargs):
    context = {

    }
    product_id = kwargs.get("pk")
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse("That product doesn't exist.")
    if product:
        context['id'] = product.id
        context['product_name'] = product.product_name
        context['description'] = product.product_descr
        context['product_image'] = product.product_image.url
        context['product_creator'] = product.product_creator
        context['product_cost'] = product.product_cost
        context['video'] = product.product_video
        context['file'] = product.product_file
        context['conspect'] = product.content
        context['content'] = product.content_tiny

    return render(request, 'ProducT/product.html', context)




# class ProductsDetailView(DetailView):
#     model = Product
#     template_name = 'ProducT/product.html'
#     context_object_name = 'ProducT'
