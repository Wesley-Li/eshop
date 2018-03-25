#!/usr/bin/env python
#coding: utf-8

from django.forms import ChoiceField
from django.utils.encoding import smart_text, force_text
from django.core.exceptions import ValidationError
from django import forms
from mezzanine.conf import settings

class WniChoiceField(ChoiceField):
    
    def validate(self, value):
        """
        Validates that the input is in self.choices.
        """
        super(ChoiceField, self).validate(value)
        if value and not self.valid_value(value):
            raise ValidationError(self.error_messages['invalid_choice'] % {'value': value})

    def valid_value(self, value):
        "Check to see if the provided value is a valid choice"
        for k, v in self.choices:
            if isinstance(v, (list, tuple)):
                # This is an optgroup, so look inside the group for options
                for k2, v2 in v:
                    if value == smart_text(k2):
                        return True
            else:
                if value == smart_text(k):
                    return True
        if value.startswith(u"预约"):
            return True
        return False

class WniChoiceWidget(forms.MultiWidget):
    def decompress(self,value):
        if value:
            #print '#'*40
            #print 'value here is:',value.encode('utf-8')
            #print 'value here is:',value
            #return [value[0],value[1]]
            try:
                return ['efoodin','xz'] if value.startswith('efoodin') else ['buyer',value]
            except Exception,e:
                print e
            #return value
        #print '*'*40
        #print 'value is:',value
        return ['efoodin',u'xz']
    
    """
    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        print '@'*40
        print 'datelist is:',datelist
        
        try:
            tmp = [datelist[0],'xz'] if datelist[0].startswith('efoodin') else ['buyer',datelist[1]]
        except ValueError:
            print '&'*40,'valueerror'
            return u'efoodin配送'
        else:
            #return settings.CENTER_POTS_DICT[tmp]
            return tmp
        
        #return datelist
    """
class WniComplexChoiceField(forms.MultiValueField):
    def __init__(self, wnichoices, max_length=80, *args, **kwargs):
        """ sets the two fields as not required but will enforce that (at least) one is set in compress """
        fields = (forms.ChoiceField(widget=forms.RadioSelect,choices=(('efoodin',u'efoodin冷链配送'),('buyer',u'站点自提')),initial="efoodin",required=False),
                  forms.ChoiceField(choices=wnichoices,required=False))
        self.widget = WniChoiceWidget(widgets=[f.widget for f in fields])
        super(WniComplexChoiceField,self).__init__(required=False,fields=fields,*args,**kwargs)
    def compress(self,data_list):
        """ return the choicefield value if selected or charfield value (if both empty, will throw exception """
        if not data_list:
            #wni:need to add here
            #print '%'*40
            #print 'data_list is:',data_list
            return "efoodin"
            #wni:comment here,on confirm page, click next, get empty value, if then, raise here, comment to work around
            #raise ValidationError('Need to select choice or enter text for this field')
        #print "^"*40
        #print data_list
        if isinstance(data_list,(list,tuple)):
            return data_list[0] if data_list[0].startswith('efoodin') else data_list[1]
        else:
            #might be bugggy here, need to verify if string or value not in POTS keys,refine later on...
            return data_list
        #return data_list[0].encode('utf-8') if data_list[0].startswith('efoodin') else data_list[1].encode('utf-8')
        #return data_list[0] or data_list[1]
        #return data_list
        #return u'efoodin冷链配送'
    
    def clean(self,value):
        """
        if value[0] != "OTHER":
            value[1] = u' '
        else:
            if value[1].strip() == u' ':
                msg = "unspecified value"
                raise forms.ValidationError(msg)
            elif "|" in value[1]:
                msg = "bad value ('|' character is not allowed)"
                raise forms.ValidationError(msg)
        return "|".join(value)
        
        return "xz"
        """
        #return self.compress(value)
        return self.compress(value)
    
    def validate(self, value):
        """
        Validates that the input is in self.choices.
        """
        #super(ChoiceField, self).validate(value)
        #if value and not self.valid_value(value):
        #    raise ValidationError(self.error_messages['invalid_choice'] % {'value': value})
        pass
    #def to_python(self,value):
    #    return 'xz'
    #def validate(self, value):
    #    return value != 'shit'
            #raise ValidationError(self.error_messages['not_an_a'])
